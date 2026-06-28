import time


class VoicePipeline:
    FORM_COOLDOWN_SECONDS = 10

    def __init__(self, llm, tts):
        self.llm = llm
        self.tts = tts
        self.last_spoken_at = 0
        self.last_spoken_issue = None

    def _find_form_issue(self, exercise, metrics):
        if "issue" in metrics:
            return metrics["issue"]

        if exercise == "Squats":
            depth = metrics.get("depth_status", "")
            back_angle = metrics.get("back_angle", 180)

            if depth == "TOO HIGH":
                return "The user's squat is not deep enough — knees are not bending sufficiently."

            if isinstance(back_angle, (int, float)) and back_angle < 130:
                return "The user is leaning too far forward during the squat."

        elif exercise == "Push-ups":
            alignment = metrics.get("body_alignment", "")
            hip_status = metrics.get("hip_status", "")

            if alignment == "Poor Form":
                return "The user's body is not straight during the push-up."

            if hip_status == "SAGGING":
                return "The user's hips are sagging down during the push-up."

            if hip_status == "PIKED UP":
                return "The user's hips are too high — lower them to form a straight line."

        elif exercise == "Biceps Curls (Dumbbell)":
            swing = metrics.get("swing_status", "")
            shoulder = metrics.get("shoulder_status", "")

            if swing == "SWINGING":
                return "The user is swinging their torso during the curl — keep the body still."

            if shoulder == "ELBOW DRIFTING":
                return "The user's elbow is drifting away from their side during the curl."

        elif exercise == "Shoulder Press":
            back_arch = metrics.get("back_arch_status", "")

            if back_arch == "Excessive Arch":
                return "The user is arching their lower back excessively during the press."

            if back_arch == "Slight Arch":
                return "Slight back arch detected — encourage the user to brace their core."

        elif exercise == "Lunges":
            balance = metrics.get("balance_status", "")

            if balance == "OFF BALANCE":
                return "The user is losing balance during the lunge — feet should be hip-width apart."

        return None

    def _should_speak_form_issue(self, issue: str, now: float) -> bool:
        if not issue:
            self.last_spoken_issue = None
            return False

        if issue == self.last_spoken_issue:
            return False

        if now - self.last_spoken_at < self.FORM_COOLDOWN_SECONDS:
            return False

        return True

    def process_event(self, event, exercise, metrics):
        issue = self._find_form_issue(exercise, metrics)
        now = time.time()
        is_major_event = event in ["workout_started", "set_completed", "workout_completed"]

        if not is_major_event:
            if event == "no_pose_detected":
                issue = issue or "No pose detected! Please step into the camera frame."

            if not self._should_speak_form_issue(issue, now):
                return None
        else:
            self.last_spoken_issue = None

        text = self.llm.give_feedback(event, issue)
        voice = self.tts.speak(text)
        if not voice:
            return None

        self.last_spoken_at = now
        if issue:
            self.last_spoken_issue = issue

        return voice, text
