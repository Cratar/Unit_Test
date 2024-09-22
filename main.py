
from GET.check_gym import test_get_pages
from POST.adding_pages import test_post_pages
from GET.check_gym import test_get_pages_json
from DELETE.deleting import test_delete_pages

def Get():
    print("\t /check/gym \t",test_get_pages("http://localhost:8089/check/gym"))
    print("\t /aut/User \t",test_get_pages_json("http://localhost:8087/aut/User" ,{"email" : "Bra@gam.vop","password" : "1235"} ))
    print("\t /aut/Admin \t",test_get_pages_json("http://localhost:8084/aut/Admin", {"email" : "favod@.go","password" : "1237"}))
    print("\t /create_table \t",test_get_pages("http://localhost:8083/create_table"))
    print("\t /create_db \t",test_get_pages("http://localhost:8083/create_db"))


    print("\n")


def Post():
    print("\t /adding/pages \t",test_post_pages("http://localhost:8082/adding/pages" ,date={

    "gym_name" : "Far",
    "address" : "Na kykah 32",
    "reservation_date" : "2024-08-27",
    "reservation_time" : "00:30:00"

}))

    print("\t /adding/pages \t",test_post_pages("http://localhost:8086/reg/User" ,date={

    "name" : "Wata",
    "surname" : "Cop",
    "email" : "Bra@gam.vop",
    "age" : "41",
    "password" : "1235"

}))

    print("\t /adding/pages \t",test_post_pages("http://localhost:8085/reg/Admin" ,date={

    "name" : "Joly",
    "surname" : "Buhach",
    "email" : "favod@.go",
    "post" : "derector",
    "age" : "52",
    "password" : "1237"

}))
    print("\n")


def Delite():
    print("\t /deleting/records \t",test_delete_pages("http://localhost:8088/deleting/records" , {"gym_name" : "Far","reservation_date" : "2024-08-27"}))

    print("\n")

if __name__ == "__main__":

        Get(),
        Post()
        Delite()





