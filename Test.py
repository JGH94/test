import New as new
import TT as tt
class MMain:
    def GuGudan(num):
        print(str(num) + "단 시작!!**********************************************")
        for z in range(1, 10):
            z_ = z;
            re_ = num * z_
            print((str(num) + "*" + str(z_) + "=" + str(re_)))


def main():
    MMain.GuGudan(5)
    re_ = new.Add(5,5)
    re2_ = new.min(5,2)
    re3_ = tt.Test("정근화TT")
    print(re3_)
if __name__ == "__main__":
    main()
