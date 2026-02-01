def chavg(stud):
    avg=0
    topper=""
    for k,v in stud.items():
        avvg=0
        avvg=sum(stud[k])/len(stud[k])
        if avvg>havg:
            havg=avvg
            topper=k
    print(f"Highest avg:{havg}")
    print(f"topper name :{topper}")
        
stscore={
    "Ram":[89,90,67],
    "laxman":[25,89,56],
    "Hanuman":[67,20]
}
chavg(stscore)