import rhinoscriptsyntax as rs


def myfavoritethings():
    things = []

    while True:
        count = len(things)
        prompt = "What is your {}th most favorite thing?".format(count+1)

        if len(things)==0:
            prompt = "What is your most favorite thing?"
        elif count==1:
            prompt = "What is your second most favorite thing?"
        elif count==2:
            prompt = "What is your third most favourite thing?"

        answer = rs.GetString(prompt)
        if answer is None: break
        things.append(answer)
    if len(things)==0: return

    print("Your", len(things)+1, "favorite things are:")
    for i,thing in enumerate(things): print(i+1, ".", thing)


if __name__=="__main__":
    myfavoritethings()