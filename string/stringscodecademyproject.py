highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

highlighted_poems_list = highlighted_poems.split(",") #splitted the string to list to make it work easy

highlighted_poems_stripped = []
for poem in highlighted_poems_list:
  highlighted_poems_stripped.append(poem.strip()) #stripped each poem for more precise 
highlighted_poems_details=[]
for poem in highlighted_poems_stripped:
  highlighted_poems_details.append(poem.split(':')) #created list inside of the list by splitting the string from :

titles=[]
poets=[]
dates=[]

for poem in highlighted_poems_details: #populating the list
  titles.append(poem[0])
  poets.append(poem[1])
  dates.append(poem[2])

for i in range(len(titles)): #formatting to display the statement with the variable string
  print("The poem {title} was published by {poet} in {date} \n".format(title=titles[i],poet=poets[i],date=dates[i]))