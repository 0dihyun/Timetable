import logging, win32com.client, sys
from win10toast import ToastNotifier

toaster = ToastNotifier()

# 프로그램 실행 검사
def isRunning(programName, isTest):
    """프로그램 작동 검사 함수

    Args:
        programName (str): 실행되는 프로그램 이름
        isTest (bool): 테스트 할 때
    """
    if isTest == True:
        logging.debug("isRunning Function: TEST MODE")
        pass
    else:
        logging.info("PROGRAM CHECKING: ···")
        wmi = win32com.client.Dispatch("WbemScripting.SWbemLocator")
        service = wmi.ConnectServer(".", "root\\cimv2")
        process_list = service.ExecQuery(f"SELECT * FROM Win32_Process WHERE Name = '{programName}'")

        while True:
            print(len(process_list))
            if len(process_list) > 0:
                toaster.show_toast(
                    "Hello!",
                    "Timetable.pyw is Running!\nNice To Meet you :)",
                    duration=3,
                    threaded=True,
                )
                logging.info("PROGRAM CHECKING: GOOD :)")
                break
            else:
                toaster.show_toast(
                    "Hello!",
                    "oh.. bad news..\nsomething went wrong.. :(",
                    duration=3,
                    threaded=True,
                )
                logging.ERROR("PROGRAM CHECKING: BAD :(")
                sys.exit()