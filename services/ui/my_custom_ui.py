import streamlit as st

def workout_not_started():
    st.html("""
        <style>
        @keyframes fadeSlideUp {
            from { opacity: 0; transform: translateY(16px); }
            to   { opacity: 1; transform: translateY(0); }
        }
        .es-wrap {
            display: flex;
            justify-content: center;
            padding: 3rem 1rem;
            animation: fadeSlideUp 0.45s ease both;
            
        }
        .es-card {
            background: #0f1117;
            border: 1px solid #2a2d3a;
            border-radius: 16px;
            padding: 52px 44px 44px;
            text-align: center;
            max-width: 600px;
            width: 100%;
            box-shadow: 0 0 20px rgba(124, 58, 237, 0.25), 0 0 40px rgba(6, 182, 212, 0.12), 0 8px 24px rgba(0, 0, 0, 0.35);
        }
        .es-icon {
            width: 56px;
            height: 56px;
            border-radius: 14px;
            background: #1e2230;
            border: 1px solid #2a2d3a;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 24px;
            font-size: 40px;
        }
        .es-title {
            font-size: 25px;
            font-weight: 600;
            color: #e2e8f0;
            margin: 0 0 10px;
            letter-spacing: -0.01em;
        }
        .es-sub {
            font-size: 20px;
            color: #64748b;
            line-height: 1.75;
            margin: 0 0 36px;
        }
        .es-sub strong { color: #94a3b8; font-weight: 500; }
        .es-divider {
            height: 1px;
            background: #1e2230;
            margin: 0 0 28px;
        }
        .es-steps {
            display: flex;
            align-items: flex-start;
            justify-content: center;
        }
        .es-step {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 8px;
            flex: 1;
            max-width: 120px;
        }
        .es-step-dot {
            width: 32px;
            height: 32px;
            border-radius: 50%;
            background: #1e2230;
            border: 1px solid #2a2d3a;
            font-size: 12px;
            font-weight: 600;
            color: #7c8ba1;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .es-step-label {
            font-size: 15px;
            color: #475569;
            text-align: center;
            line-height: 1.4;
        }
        .es-connector {
            flex: 0 0 32px;
            height: 1px;
            background: #2a2d3a;
            margin-top: 16px;
        }
        </style>

        <div class="es-wrap">
          <div class="es-card">
            <div class="es-icon">🏋️</div>
            <div class="es-title">Set up your workout</div>
            <p class="es-sub">
              Use the sidebar to choose your exercise,<br>
              configure sets and reps, then click<br>
              <strong>Start Workout</strong> to launch the AI coach.
            </p>
            <div class="es-divider"></div>
            <div class="es-steps">
              <div class="es-step">
                <div class="es-step-dot">1</div>
                <div class="es-step-label">Pick exercise</div>
              </div>
              <div class="es-connector"></div>
              <div class="es-step">
                <div class="es-step-dot">2</div>
                <div class="es-step-label">Set reps &amp; sets</div>
              </div>
              <div class="es-connector"></div>
              <div class="es-step">
                <div class="es-step-dot">3</div>
                <div class="es-step-label">Start workout</div>
              </div>
            </div>
          </div>
        </div>
    """)