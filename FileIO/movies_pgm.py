f=open("movies.csv", "r")

movie_data={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    name=data[1].rstrip("***").lower()
    year=data[2]
    rating=data[3]
    views=data[4]
    if name not in movie_data:
        movie_data[name]= {
            "name":name,
            "year":year,
            "rating":rating,
            "views":views
        }
    else:
        movie_data[name] ={
            "name":name,
            "year": year,
            "rating": rating,
            "views": views
        }


i=0
for k,v in movie_data.items():
      if i==5:
          break
      print(k,v)
# list=[(k,v)for  k,v in dict.items(rgs)]
# print(list)

# def print_movie_data(**kwargs):
#     name=kwargs.get("name")
#     if name in movie_data:
#         print(name,movie_data[name]["year"])
#         if property in kwargs:
#             prop=kwargs["property"]
#             if prop in movie_data[name]:
#                 print(prop,"=>",movie_data[name][prop])
#     else:
#         print("there  is  no movie in that year")
#
#
# print_movie_data(name="The Mummy",property="year")

