#coding = utf-8
'''
此模块用来读取excel文件中的内容（以第几行，第几列的方法读）
'''
from public.utils.ReadExcel import ReadExcel
class Login_Data:
    #静态方法，可以直接被类调用
    @staticmethod
    def get_url():
        #1和0必须为索引值（第二行，第一列）
        url = ReadExcel("Data.xlsx","Sheet1").read_excel(1,0)
        # print(url)
        return url

    @staticmethod
    def get_username():
        username = ReadExcel("Data.xlsx","Sheet1").read_excel(1,1)
        # print(username)
        return username

    @staticmethod
    def get_code():
        code = ReadExcel("Data.xlsx","Sheet1").read_excel(1,2)
        # print(code)
        return int(code)

    @staticmethod
    def get_pwd():
        pwd = ReadExcel("Data.xlsx","Sheet1").read_excel(1,3)
        # print(pwd)
        return pwd
    @staticmethod
    def get_login_success():
        login_success = ReadExcel("Data.xlsx","Sheet1").read_excel(1,4)
        return login_success


if __name__ == '__main__':
    # 因为是静态方法，所以可以直接类.方法的形式来调用
    print(Login_Data.get_url())
    print(Login_Data.get_username())
    print(Login_Data.get_code())
    print(Login_Data.get_pwd())
    print(Login_Data.get_login_success())