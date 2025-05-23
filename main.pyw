if __name__ == "__main__":
    import os
    import sys
    import threading
    import subprocess
    
    req_file = "requirements.txt"
    
    # requirements 설치
    if not os.getenv("REQUIREMENTS_INSTALLED"):
        if os.path.exists(req_file):
            subprocess.run([sys.executable, "-m", "pip", "install", "-r", req_file], check=True)

            os.environ["REQUIREMENTS_INSTALLED"] = "1"

            os.execl(sys.executable, sys.executable, *sys.argv)
            sys.exit()
    
    from function.main_functions import program_running_check, notificationFunc
    from function.system_tray import systemTray

    # 프로그램 실행 체크
    program_running_check()

    # timetableReminderFunc 백그라운드에서 단독 실행
    timetableReminderFunc = threading.Thread(target=notificationFunc, daemon=True)
    timetableReminderFunc.start()

    # system tray 설정
    app = systemTray()
    app.run()
