import shape


while True:
    def main():
        print("Choose a shape to calculate its area:")
        print("1. Circle")
        print("2. Rectangle")
        print("3. Triangle")
        print("4. Exit")


        choice = input("Enter your choice (1/2/3/4): ")
        
        
        try:
            if choice == '1':
                radius = float(input("Enter the radius of the circle: "))
                area = shape.area_circle(radius)
                print(f"The area of the circle is: {area:.2f}") 
                print("-" * 40)

            elif choice == '2':
                length = float(input("Enter the length of the rectangle: "))
                width = float(input("Enter the width of the rectangle: "))  
                area_rect = shape.area_rectangle(length, width)
                print(f"The area of the rectangle is: {area_rect:.2f}")
                print("-" * 40)

            elif choice == '3':
                base = float(input("Enter the base of the triangle: "))
                height = float(input("Enter the height of the triangle: "))
                area_tri = shape.area_triangle(base, height)
                print(f"The area of the triangle is: {area_tri:.2f}")
                print("-" * 40)

            elif choice == '4':
                print("Exiting the program. Goodbye!")
                print("-" * 40)

            else:
                print("Invalid choice. Please select a valid option.")
                print("-" * 40)



        except ValueError as e:
            print(f"Error: {e}")

    if __name__ == "__main__":
        main()