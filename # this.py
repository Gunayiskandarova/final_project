name=[]
rating=[]

def main():
    while True:
        info()
        n=int(input())
        if n==1:
            add_movie()
        elif n==2:
            rating_movie
        print("press 1 to input movies")
        print("press 2 to display movies and ratings ")
        print("press 0 to exit")
        choise=int((input))
        if choise=="1":
            for i in range(3):
                i