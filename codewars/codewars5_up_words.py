def to_jaden_case(string):
    new=string.title()
    if "'" in new:
        ber = new.find("'")
    new_one = new.replace(new[ber+1],new[ber+1].lower())

    print(new_one)



to_jaden_case("How can mirrors be real if our eyes aren't real")