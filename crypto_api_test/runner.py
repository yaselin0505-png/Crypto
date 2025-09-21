import os
import sys

def run_feature():
    print('******run features******')
    run_result = os.system("behave --tags=@normaltest -f allure_behave.formatter:AllureFormatter -o ./test_report ./features")
    print(f"result is {str(run_result)}")
    report_status=os.system("allure generate ./test_report --clean -o ./test_report/allure_html")
    print(f"result is {str(report_status)}")

    if run_result == 0 and report_status == 0:
        print("*******generate report success*******")
        sys.exit(0)
    else:
        print("*******generate report fail*******")
        print("run_result:{}".format(run_result))
        print("report_status:{}".format((report_status)))
        sys.exit(1)

if __name__ == '__main__':
    run_feature()