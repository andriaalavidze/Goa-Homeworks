def find_short(s):
    list1 = s.split(" ")

    word_len = len(list1[0])
    for i in list1:
        if len(i) < word_len:
            word_len = len(i)
    
    # word_len = 3
    return word_len

print(find_short("bitcoin take over the world maybe who knows perhaps"))

# ფუნქციაში თავიდან შევქმენით ცვლადი სახელად
# list1 რომელსაც გადავეცით s ანუ რაღაც გრძელი
# სტრინგი და ს-ის გვერძე გამოვიყენეთ split ფუნქცია
# სადაც ჩავსვით სფეისი ანუ ამ დიდ წინადადებაში 
# სადაც სფეისი იქნებოდა იქამდე შედგებოდა 1 სტრინგი
# შემდეგ შევქმენით ცვლადი word_len და მასში len
# ფუნქციის საშვალებით ამ list1-ის პირველი წევრის
# ასოების რაოდენობა ჩავსვით რაც გამოვიდოდა 7 
# შემდეგ გადავუარეთ სიას და თუ რომელიმე უფრო
# ცოტა ასოსგან შედგებოდა ვიდრე word_len-ში ჩასმული
# სიტვის ასოთა რაოდენობა ჩანაცვლებულიყო word_len
# ამ ახალი სტრინგის ასოთა რაოდენობით ჩვენ ამით
# გავარკვიეთ ყველაზე პატარა სტრინგი ამ წინადადებაში
# რამდენი ასოსგან შედგებოდა