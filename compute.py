import pandas as pd
import plotly_express as px

import networkx as nx
import osmnx as ox
import os, time, glob

def create_graph(loc, dist, transport_mode, loc_type="address"):
    """Transport mode = ‘walk’, ‘bike’, ‘drive’, ‘drive_service’, ‘all’, ‘all_private’, ‘none’"""
    if loc_type == "address":
        G = ox.graph_from_address(loc, dist=dist, network_type=transport_mode)
    elif loc_type == "points":
        G = ox.graph_from_point(loc, dist=dist, network_type=transport_mode )
    return G
    
  
def compute(A_Lat, A_Long, B_Lat, B_Long):
    G = create_graph('3500 Oleander Dr,Wilmington, NC', 1000, "drive")    
    G = ox.add_edge_speeds(G) #Line we will modify for the stochastic model
    G = ox.add_edge_travel_times(G)

    #start = (A_Lat, A_Long)
    #end =   (B_Lat, B_Long)
    #start_node = ox.get_nearest_node(G, start) 
    #end_node = ox.get_nearest_node(G, end)
    
    #route = nx.shortest_path(G, start_node, end_node, weight='travel_time')

    return [0,1,2,3]#route