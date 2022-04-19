def route(duration = 10):

    """
    The function gives all the possible trains/busses etc.
    """
    import requests
    departure = input('\nWhich station is the departure point:\n')
    url = f"https://v5.vbb.transport.rest/locations?poi=false&addresses=false&query={departure}"
    station_id = requests.get(url).json()[0]['id']
    print(f'\nNext connections from {departure}:\n')
    url = f'https://v5.vbb.transport.rest/stops/{station_id}/departures?duration={duration}'
    my_url_list = requests.get(url).json()
    for choises in my_url_list:
        print(choises['plannedWhen'][11:-9], '  ', choises['line']['name'], choises['direction'],'. There are',round(choises['delay']/60,0),' min delay.')



# if __name__ == '__main__':  # this is for defining things
#     route(number_of_list=10)