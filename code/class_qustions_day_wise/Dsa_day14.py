'''
Insertion Sort
(S|US)

time complexity  of insertion sort is f(n2)

'''
# var = [7, 3, 5, 9, 2, 12]

# def insertion_sort(var):
#     for i in range(1, len(var)):
#         value = var[i]
#         j = i - 1
#         while j >= 0 and var[j] > value:
#             var[j+1] = var[j]
#             j -= 1
#         var[j+1] = value


# insertion_sort(var)
# print(var)


'''Quick sort:
   (p|LS|RG)
'''
# one code for recurion
#  using  to solve it


# var = [7, 3, 5, 9, 2, 15]

# def quick_sort(var):
#     if len(var) <= 1:
#         return var
#     pivot = var[len(var) // 2]
#     left = [x for x in var if x < pivot]
#     middle = [x for x in var if x == pivot]
#     right = [x for x in var if x > pivot]
#     return quick_sort(left) + middle + quick_sort(right)


# var = quick_sort(var)
# print(var)



# solveing it using loop to solve it

# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = []
#     middle = []
#     right = []

#     # Using loop
#     for i in arr:
#         if i < pivot:
#             left.append(i)
#         elif i == pivot:
#             middle.append(i)
#         else:
#             right.append(i)
#     return quick_sort(left) + middle + quick_sort(right)

# arr = [7, 3, 5, 9, 2, 15]
# print("Original Array:", arr)
# sorted_arr = quick_sort(arr)
# print("Sorted Array:", sorted_arr)
    



'''An airline wants to manage routes between cities.
Requirements:
    create a graph where each city is connected to its direct flight destinations.
    Display all available routes.
    Store all city names in a list.
    Sort the city names alphabetically using Insertion sort.
    Ask the user to search for city using Binary Search.
    If found, display cities directly connect to it.
    Otherwise, display "City not found."
    '''
# class Graph:
#     def __init__(self):
#         self.graph = {}
#         self.cities = []
#     def add_city(self, city):
#         if city not in self.graph:
#             self.graph[city] = []
#             self.cities.append(city)
#     def add_route(self, city1, city2):
#         if city1 in self.graph and city2 in self.graph:
#             self.graph[city1].append(city2)
#     def display_routes(self):
#         for city, location in self.graph.items():
#             print(f"{city} - {','.join(location)}")
#     def insertion_sort(self):
#         for i in range(1, len(self.cities)):
#             value = self.cities[i]
#             j = i - 1
#             while j >= 0 and self.cities[j] > value:
#                 self.cities[j + 1] = self.cities[j]
#                 j -= 1
#             self.cities[j + 1] = value
#     def binary_search(self, city):
#         left, right = 0, len(self.cities) - 1
#         while left <= right:
#             mid_value = (left + right) // 2
#             if self.cities[mid_value] == city:
#                 return mid_value
#             elif self.cities[mid_value] < city:
#                 left = mid_value + 1
#             else:
#                 right = mid_value -1
#         return -1 

#     def display_cities(self):
#         print("Cities in aplhabetical order:")
#         for city in self.cities:
#             print(city)



# graph = Graph()
# print("Enter the number of cities: ")
# num_cities = int(input())

# for i in range(num_cities):
#     city = input(f"Enter city{i + 1}: ")
#     graph.add_city(city)

# graph.insertion_sort()
# graph.display_cities()



# question 2

'''
A social meadia platform stores friendships between users.

requirements:
    create a graph where each user is connected to their friends.
    Display all users and their friends in a formated way.
    Store all user names in a list.
    Sort the user names using Insertion sort.
    Ask the user to search for a user using Binary Search.
    If found, display the user's friends.
    Otherwise, display "User not found."
'''

# import matplotlib.pyplot as plt
# import networkx as nx

# # Create graph
# graph = nx.Graph()

# graph.add_edge("Amit", "Abhay")
# graph.add_edge("Tavi", "Arya")
# graph.add_edge("Ravi", "Amit")
# graph.add_edge("Abhay", "Ravi")
# graph.add_edge("Arya", "Tavi")
# graph.add_edge("Amit", "Arya")
# graph.add_edge("Ravi", "Tavi")

# nx.draw(
#     graph,
#     with_labels=True,
#     node_color="lightblue",
#     node_size=2000,
#     font_size=10,
#     font_color="black"
# )

# plt.title("Social Media Friendship Graph")
# plt.show()



'''
rich library to display the graph in a table format

'''


# from rich.console import Console
# from rich.table import Table

# console = Console()

# graph = {
#     "Amit": ["Rahul", "Arya"],
#     "Rahul": ["Amit", "Neha"],
#     "Arya": ["Amit"],
#     "Neha": ["Rahul"]
# }

# table = Table(title="Social Media Friendships")

# table.add_column("User", style="cyan")
# table.add_column("Friends", style="green")

# for user, friends in graph.items():
#     table.add_row(user, ", ".join(friends))

# console.print(table)


''' using tkinter to display the graph in a GUI format'''

# import tkinter as tk
# from tkinter import messagebox
# import networkx as nx
# import matplotlib.pyplot as plt

# graph = nx.Graph()


# def add_friendship():
#     user1 = entry1.get().strip()
#     user2 = entry2.get().strip()

#     if user1 == "" or user2 == "":
#         messagebox.showerror("Error", "Enter both user names")
#         return

#     graph.add_edge(user1, user2)

#     listbox.insert(tk.END, f"{user1} ↔ {user2}")

#     entry1.delete(0, tk.END)
#     entry2.delete(0, tk.END)


# def show_graph():
#     plt.figure(figsize=(6, 5))
#     nx.draw(
#         graph,
#         with_labels=True,
#         node_color="lightblue",
#         node_size=2000,
#         font_size=10,
#         font_color="black"
#     )
#     plt.title("Social Media Friendship Graph")
#     plt.show()


# root = tk.Tk()
# root.title("Social Media Platform")
# root.geometry("400x400")

# tk.Label(root, text="User 1").pack()
# entry1 = tk.Entry(root)
# entry1.pack()

# tk.Label(root, text="User 2").pack()
# entry2 = tk.Entry(root)
# entry2.pack()

# tk.Button(root, text="Add Friendship", command=add_friendship).pack(pady=10)

# tk.Button(root, text="Show Graph", command=show_graph).pack(pady=10)

# listbox = tk.Listbox(root, width=40)
# listbox.pack(pady=10)

# root.mainloop()

'''Solving this kivy to solving this '''

# import kivy
# kivy.require("2.3.0")

# from kivy.app import App
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.button import Button
# from kivy.uix.label import Label
# from kivy.uix.textinput import TextInput

# import networkx as nx
# import matplotlib.pyplot as plt


# class SocialMediaApp(App):

#     def build(self):

#         self.graph = nx.Graph()
#         self.users = []

#         layout = BoxLayout(
#             orientation="vertical",
#             padding=10,
#             spacing=10
#         )

#         # Add friendship
#         self.user1 = TextInput(
#             hint_text="Enter User 1",
#             multiline=False
#         )

#         self.user2 = TextInput(
#             hint_text="Enter User 2",
#             multiline=False
#         )

#         layout.add_widget(self.user1)
#         layout.add_widget(self.user2)

#         add_btn = Button(text="Add Friendship")
#         add_btn.bind(on_press=self.add_friend)

#         layout.add_widget(add_btn)

#         # Search User
#         self.search_box = TextInput(
#             hint_text="Search User",
#             multiline=False
#         )

#         layout.add_widget(self.search_box)

#         search_btn = Button(text="Search User")
#         search_btn.bind(on_press=self.search_user)

#         layout.add_widget(search_btn)

#         # Show Graph
#         graph_btn = Button(text="Show Friendship Graph")
#         graph_btn.bind(on_press=self.show_graph)

#         layout.add_widget(graph_btn)

#         # Show All Friendships
#         display_btn = Button(text="Display All Friendships")
#         display_btn.bind(on_press=self.display_friendships)

#         layout.add_widget(display_btn)

#         self.output = Label(
#             text="Welcome",
#             halign="left",
#             valign="top"
#         )

#         layout.add_widget(self.output)

#         return layout

#     # ---------------- Add Friendship ----------------

#     def add_friend(self, instance):

#         u1 = self.user1.text.strip()
#         u2 = self.user2.text.strip()

#         if u1 == "" or u2 == "":
#             self.output.text = "Enter both users."
#             return

#         self.graph.add_edge(u1, u2)

#         if u1 not in self.users:
#             self.users.append(u1)

#         if u2 not in self.users:
#             self.users.append(u2)

#         self.output.text = f"{u1} and {u2} are now friends."

#         self.user1.text = ""
#         self.user2.text = ""

#     # ---------------- Display Friendships ----------------

#     def display_friendships(self, instance):

#         text = ""

#         for user in self.graph.nodes():

#             friends = list(self.graph.neighbors(user))

#             text += f"{user} -> {', '.join(friends)}\n"

#         self.output.text = text

#     # ---------------- Insertion Sort ----------------

#     def insertion_sort(self):

#         for i in range(1, len(self.users)):

#             key = self.users[i]
#             j = i - 1

#             while j >= 0 and self.users[j] > key:
#                 self.users[j + 1] = self.users[j]
#                 j -= 1

#             self.users[j + 1] = key

#     # ---------------- Binary Search ----------------

#     def binary_search(self, name):

#         left = 0
#         right = len(self.users) - 1

#         while left <= right:

#             mid = (left + right) // 2

#             if self.users[mid] == name:
#                 return mid

#             elif self.users[mid] < name:
#                 left = mid + 1

#             else:
#                 right = mid - 1

#         return -1

#     # ---------------- Search User ----------------

#     def search_user(self, instance):

#         self.insertion_sort()

#         user = self.search_box.text.strip()

#         index = self.binary_search(user)

#         if index != -1:

#             friends = list(self.graph.neighbors(user))

#             if len(friends) == 0:
#                 self.output.text = f"{user} has no friends."

#             else:
#                 self.output.text = f"{user}'s Friends:\n" + ", ".join(friends)

#         else:

#             self.output.text = "User not found."

#     # ---------------- Draw Graph ----------------

#     def show_graph(self, instance):

#         plt.figure(figsize=(6, 5))

#         nx.draw(
#             self.graph,
#             with_labels=True,
#             node_size=2500,
#             node_color="lightgreen",
#             font_size=10,
#             font_weight="bold"
#         )

#         plt.title("Social Media Friendship Graph")

#         plt.show()


# if __name__ == "__main__":
#     SocialMediaApp().run()



'''Cherrypy using make it '''

# import cherrypy


# class SocialMedia:

#     def __init__(self):
#         self.graph = {}
#         self.users = []

#     # ---------------- Add User ----------------

#     def add_user(self, user):
#         if user not in self.graph:
#             self.graph[user] = []
#             self.users.append(user)

#     # ---------------- Add Friendship ----------------

#     def add_friend(self, user1, user2):

#         self.add_user(user1)
#         self.add_user(user2)

#         if user2 not in self.graph[user1]:
#             self.graph[user1].append(user2)

#         if user1 not in self.graph[user2]:
#             self.graph[user2].append(user1)

#     # ---------------- Insertion Sort ----------------

#     def insertion_sort(self):

#         for i in range(1, len(self.users)):

#             key = self.users[i]
#             j = i - 1

#             while j >= 0 and self.users[j] > key:
#                 self.users[j + 1] = self.users[j]
#                 j -= 1

#             self.users[j + 1] = key

#     # ---------------- Binary Search ----------------

#     def binary_search(self, name):

#         left = 0
#         right = len(self.users) - 1

#         while left <= right:

#             mid = (left + right) // 2

#             if self.users[mid] == name:
#                 return mid

#             elif self.users[mid] < name:
#                 left = mid + 1

#             else:
#                 right = mid - 1

#         return -1

#     # ---------------- Home Page ----------------

#     @cherrypy.expose
#     def index(self):

#         return """
#         <html>

#         <head>

#         <title>Social Media Platform</title>

#         </head>

#         <body>

#         <h1>Social Media Friendship System</h1>

#         <hr>

#         <h3>Add Friendship</h3>

#         <form action="add">

#         User 1 :
#         <input type="text" name="u1">

#         <br><br>

#         User 2 :
#         <input type="text" name="u2">

#         <br><br>

#         <input type="submit" value="Add Friendship">

#         </form>

#         <hr>

#         <h3>Search User</h3>

#         <form action="search">

#         User Name :
#         <input type="text" name="name">

#         <input type="submit" value="Search">

#         </form>

#         <hr>

#         <a href="display">Display All Friendships</a>

#         </body>

#         </html>
#         """

#     # ---------------- Add Friendship ----------------

#     @cherrypy.expose
#     def add(self, u1, u2):

#         self.add_friend(u1, u2)

#         return f"""
#         <html>

#         <body>

#         <h2>Friendship Added Successfully</h2>

#         <p>{u1} ↔ {u2}</p>

#         <br>

#         <a href="/">Home</a>

#         </body>

#         </html>
#         """

#     # ---------------- Display ----------------

#     @cherrypy.expose
#     def display(self):

#         self.insertion_sort()

#         text = """
#         <html>

#         <body>

#         <h2>All Users and Friends</h2>

#         <table border="1" cellpadding="8">

#         <tr>

#         <th>User</th>

#         <th>Friends</th>

#         </tr>
#         """

#         for user in self.users:

#             friends = ", ".join(self.graph[user])

#             if friends == "":
#                 friends = "No Friends"

#             text += f"""
#             <tr>

#             <td>{user}</td>

#             <td>{friends}</td>

#             </tr>
#             """

#         text += """
#         </table>

#         <br>

#         <a href="/">Home</a>

#         </body>

#         </html>
#         """

#         return text

#     # ---------------- Search ----------------

#     @cherrypy.expose
#     def search(self, name):

#         self.insertion_sort()

#         index = self.binary_search(name)

#         if index == -1:

#             return """
#             <html>

#             <body>

#             <h2>User not found.</h2>

#             <br>

#             <a href="/">Home</a>

#             </body>

#             </html>
#             """

#         friends = ", ".join(self.graph[name])

#         if friends == "":
#             friends = "No Friends"

#         return f"""
#         <html>

#         <body>

#         <h2>User Found</h2>

#         <p><b>Name :</b> {name}</p>

#         <p><b>Friends :</b> {friends}</p>

#         <br>

#         <a href="/">Home</a>

#         </body>

#         </html>
#         """


# if __name__ == "__main__":

#     app = SocialMedia()

#     cherrypy.config.update({
#         "server.socket_host": "127.0.0.1",
#         "server.socket_port": 8081
#     })

#     cherrypy.quickstart(app)