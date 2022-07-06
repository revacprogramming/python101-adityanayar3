
lst=[]
def get_cs():
    """get string input"""
  str=input("Enter a string")


def cs_to_lot(cs):
    """convert connected string to list of strings"""
  lst=str.split()
  

def main():
    cs = get_cs()

    lot = cs_to_lot(cs)
    print(lot)


if __name__ == '__main__':
    main()
