from menu import menu

def main():
    try:
        menu()
    except Exception as e:
        print(e)
        
if __name__ == "__main__":
    main()