def get_age():
    age = int(input("Enter an age: "))
    if age < 18 or age > 75:
        raise ValueError('Invalid age.')
    return age

def fat_burning_heart_rate(age):
    heart_rate = (220 - age) * .70
    return heart_rate

if __name__ == "__main__":
    age = get_age()
        
    heart_rate = fat_burning_heart_rate(age)
    print(f'Fat burning heart rate for a { age } year-old: { heart_rate } bpm')

    