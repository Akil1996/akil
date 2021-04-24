from .p1xp2exact import *
import plotly.graph_objs as go
import plotly.offline as opy



# def graph_df_to_list(df):
#
#     lst_a = df.iloc[:, 0].to_list()
#     lst_b = df.iloc[:, 1].to_list()
#
#     return lst_a, lst_b

def graph_point_distance(distance_df, distance_planets_df,graph_planets, graph_degree):
    df1= distance_df.copy()
    df2 = distance_planets_df.copy()
    df1["Su_dp_lst"] = df2.Su_dp_lst.to_list()
    df1["Mo_dp_lst"] = df2.Mo_dp_lst.to_list()
    df1["Me_dp_lst"] = df2.Me_dp_lst.to_list()
    df1["Ma_dp_lst"] = df2.Ma_dp_lst.to_list()
    df1["Ju_dp_lst"] = df2.Ju_dp_lst.to_list()
    df1["Ve_dp_lst"] = df2.Ve_dp_lst.to_list()
    df1["Sa_dp_lst"] = df2.Sa_dp_lst.to_list()
    df1["Ra_dp_lst"] = df2.Ra_dp_lst.to_list()
    df1["Ke_dp_lst"] = df2.Ke_dp_lst.to_list()
    df1["As_dp_lst"] = df2.As_dp_lst.to_list()
    df1 = df1.set_index("type")
    if graph_planets == "Su":
        temp_df = (df1.loc[:, ["Su_Dis_lst", "Su_dp_lst"]])
        if graph_degree == "Conj":
            return (temp_df.loc["Conj"])
        if graph_degree == "180":
            return (temp_df.loc["180"])
        if graph_degree == "120<":
            return (temp_df.loc["120<"])
        if graph_degree == ">120":
            return (temp_df.loc[">120"])
        if graph_degree == "90<":
            return (temp_df.loc["90<"])
        if graph_degree == ">90":
            return (temp_df.loc[">90"])
        if graph_degree == "60<":
            return (temp_df.loc["60<"])
        if graph_degree == ">60":
            return (temp_df.loc[">60"])

    if graph_planets == "Mo":
        temp_df = (df1.loc[:, ["Mo_Dis_lst", "Mo_dp_lst"]])
        if graph_degree == "Conj":
            return (temp_df.loc["Conj"])
        if graph_degree == "180":
            return (temp_df.loc["180"])
        if graph_degree == "120<":
            return (temp_df.loc["120<"])
        if graph_degree == ">120":
            return (temp_df.loc[">120"])
        if graph_degree == "90<":
            return (temp_df.loc["90<"])
        if graph_degree == ">90":
            return (temp_df.loc[">90"])
        if graph_degree == "60<":
            return (temp_df.loc["60<"])
        if graph_degree == ">60":
            return (temp_df.loc[">60"])

    if graph_planets == "Me":
        temp_df = (df1.loc[:, ["Me_Dis_lst", "Me_dp_lst"]])
        if graph_degree == "Conj":
            return (temp_df.loc["Conj"])
        if graph_degree == "180":
            return (temp_df.loc["180"])
        if graph_degree == "120<":
            return (temp_df.loc["120<"])
        if graph_degree == ">120":
            return (temp_df.loc[">120"])
        if graph_degree == "90<":
            return (temp_df.loc["90<"])
        if graph_degree == ">90":
            return (temp_df.loc[">90"])
        if graph_degree == "60<":
            return (temp_df.loc["60<"])
        if graph_degree == ">60":
            return (temp_df.loc[">60"])
    if graph_planets == "Ma":
        temp_df = (df1.loc[:, ["Ma_Dis_lst", "Ma_dp_lst"]])
        if graph_degree == "Conj":
            return (temp_df.loc["Conj"])
        if graph_degree == "180":
            return (temp_df.loc["180"])
        if graph_degree == "120<":
            return (temp_df.loc["120<"])
        if graph_degree == ">120":
            return (temp_df.loc[">120"])
        if graph_degree == "90<":
            return (temp_df.loc["90<"])
        if graph_degree == ">90":
            return (temp_df.loc[">90"])
        if graph_degree == "60<":
            return (temp_df.loc["60<"])
        if graph_degree == ">60":
            return (temp_df.loc[">60"])
    if graph_planets == "Ju":
        temp_df = (df1.loc[:, ["Ju_Dis_lst", "Ju_dp_lst"]])
        if graph_degree == "Conj":
            return (temp_df.loc["Conj"])
        if graph_degree == "180":
            return (temp_df.loc["180"])
        if graph_degree == "120<":
            return (temp_df.loc["120<"])
        if graph_degree == ">120":
            return (temp_df.loc[">120"])
        if graph_degree == "90<":
            return (temp_df.loc["90<"])
        if graph_degree == ">90":
            return (temp_df.loc[">90"])
        if graph_degree == "60<":
            return (temp_df.loc["60<"])
        if graph_degree == ">60":
            return (temp_df.loc[">60"])

    if graph_planets == "Ve":
        temp_df = (df1.loc[:, ["Ve_Dis_lst", "Ve_dp_lst"]])
        if graph_degree == "Conj":
            return (temp_df.loc["Conj"])
        if graph_degree == "180":
            return (temp_df.loc["180"])
        if graph_degree == "120<":
            return (temp_df.loc["120<"])
        if graph_degree == ">120":
            return (temp_df.loc[">120"])
        if graph_degree == "90<":
            return (temp_df.loc["90<"])
        if graph_degree == ">90":
            return (temp_df.loc[">90"])
        if graph_degree == "60<":
            return (temp_df.loc["60<"])
        if graph_degree == ">60":
            return (temp_df.loc[">60"])

    if graph_planets == "Sa":
        temp_df = (df1.loc[:, ["Sa_Dis_lst", "Sa_dp_lst"]])
        if graph_degree == "Conj":
            return (temp_df.loc["Conj"])
        if graph_degree == "180":
            return (temp_df.loc["180"])
        if graph_degree == "120<":
            return (temp_df.loc["120<"])
        if graph_degree == ">120":
            return (temp_df.loc[">120"])

        if graph_degree == "90<":
            return (temp_df.loc["90<"])
        if graph_degree == ">90":
            return (temp_df.loc[">90"])
        if graph_degree == "60<":
            return (temp_df.loc["60<"])
        if graph_degree == ">60":
            return (temp_df.loc[">60"])

    if graph_planets == "Ra":
        temp_df = (df1.loc[:, ["Ra_Dis_lst", "Ra_dp_lst"]])
        if graph_degree == "Conj":
            return (temp_df.loc["Conj"])
        if graph_degree == "180":
            return (temp_df.loc["180"])
        if graph_degree == "120<":
            return (temp_df.loc["120<"])
        if graph_degree == ">120":
            return (temp_df.loc[">120"])
        if graph_degree == "90<":
            return (temp_df.loc["90<"])
        if graph_degree == ">90":
            return (temp_df.loc[">90"])
        if graph_degree == "60<":
            return (temp_df.loc["60<"])
        if graph_degree == ">60":
            return (temp_df.loc[">60"])

    if graph_planets == "Ke":
        temp_df = (df1.loc[:, ["Ke_Dis_lst", "Ke_dp_lst"]])
        if graph_degree == "Conj":
            return (temp_df.loc["Conj"])
        if graph_degree == "180":
            return (temp_df.loc["180"])
        if graph_degree == "120<":
            return (temp_df.loc["120<"])
        if graph_degree == ">120":
            return (temp_df.loc[">120"])
        if graph_degree == "90<":
            return (temp_df.loc["90<"])
        if graph_degree == ">90":
            return (temp_df.loc[">90"])
        if graph_degree == "60<":
            return (temp_df.loc["60<"])
        if graph_degree == ">60":
            return (temp_df.loc[">60"])

    if graph_planets == "As":
        temp_df = (df1.loc[:, ["As_Dis_lst", "As_dp_lst"]])
        if graph_degree == "Conj":
            return (temp_df.loc["Conj"])
        if graph_degree == "180":
            return (temp_df.loc["180"])
        if graph_degree == "120<":
            return (temp_df.loc["120<"])
        if graph_degree == ">120":
            return (temp_df.loc[">120"])
        if graph_degree == "90<":
            return (temp_df.loc["90<"])
        if graph_degree == ">90":
            return (temp_df.loc[">90"])
        if graph_degree == "60<":
            return (temp_df.loc["60<"])
        if graph_degree == ">60":
            return (temp_df.loc[">60"])

def generate_graph(graph_pd_df):
    planets = ["Su", "Mo", "Me", "Ma", "Ju", "Ve", "Sa", "Ra", "Ke","As"]
    lst_a = graph_pd_df.iloc[:, 0].to_list()
    lst_b = graph_pd_df.iloc[:, 1].to_list()
    fig = go.Figure(
        data=[
            go.Bar(name='Distance', x=planets, y=lst_a),
            go.Bar(name='Points', x=planets, y=lst_b)
        ],
        layout=go.Layout(
            title="ASPECTS OF PERSON 1 OVER PLANETS OF PERSON 2",
            yaxis_title="Values"
        )
    )
    fig.update_layout(barmode='group')

    bar_div = opy.plot(fig, auto_open=False, output_type='div')
    return bar_div


def graph_main(graph_planets, graph_degree):
    constants_start_and_end_limit = constants_limit_for_sign()
    eve_person_one = event_person(constants_start_and_end_limit, 331, 232, 290, 274, 305, 354, 332, 280, 100, 80)
    eve_person_two = event_person(constants_start_and_end_limit, 9.02, 326.45, 341.82, 349.05, 96.68, 336.65, 133.73,
                                  141.72, 321.72, 318.28)
    house_df = house_table(eve_person_one)
    house_sign_df = house_and_sign(house_df)
    sign_house_df = sign_and_house(house_sign_df)
    sign_planet_house_df = sign_planet_and_house(eve_person_one, sign_house_df)
    pasp_table_df = pasp_table_degs()
    sign_table_df = sign_table_degs()
    sep_degree_df = sep_degree_p1p2(eve_person_one, eve_person_two)
    con_sign_planet_df = concatenation_sign_house(sign_planet_house_df, pasp_table_df, sign_table_df, eve_person_two)
    single_concatenation_df = single_concatenation_table(sign_planet_house_df)
    single_point_df = single_points_table(single_concatenation_df)
    point_planet_aspects_df = point_planets_planet_aspects(single_point_df)
    point_df = points_table(con_sign_planet_df, point_planet_aspects_df)
    distance_df = distance_table(point_df, sep_degree_df)
    dm_data_df = dm_data()
    distance_planets_df = distance_between_planets(distance_df, dm_data_df)
    interaccion_df = interaccion(distance_planets_df)
    p1p2recibe_df = p1p2recibe(interaccion_df)
    graph_pd_df = graph_point_distance(distance_df,distance_planets_df, graph_planets, graph_degree)
    bar_div =generate_graph(graph_pd_df)
    main_dic = {"bar_div": bar_div}
    return main_dic