import vincent

def bar_graph():
    list_data = [10, 20, 30, 20, 15, 30, 45]
    bar = vincent.Bar(list_data)
    bar.to_json('bar.json')

if __name__ == '__main__':
   bar_graph()