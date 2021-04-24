from django.shortcuts import render
import json
from django.shortcuts import render

from .excelex import readdm
from .p1conp2 import p1vsp2_main
from .personone import p1main
from .p1xp2exact import p1xp2ex_main
from .ax_report import graph_main


degree_dic = {"p1_su_degree": 331, "p1_mo_degree": 232, "p1_me_degree": 290, "p1_ma_degree": 274, "p1_ju_degree": 305.43,
                  "p1_ve_degree": 354, "p1_sa_degree": 332, "p1_ra_degree": 280, "p1_ke_degree": 100, "p1_as_degree": 80,
                  "p2_su_degree": 9.01666666666667, "p2_mo_degree": 326.45, "p2_me_degree": 341.816666666667, "p2_ma_degree": 349.05, "p2_ju_degree": 96.6833333333333,
                  "p2_ve_degree": 336.65, "p2_sa_degree": 133.73, "p2_ra_degree": 141.72, "p2_ke_degree": 321.71, "p2_as_degree": 318.28,
                  }

def p2pform(request):
    global degree_dic
    if (request.method == 'POST'):
        p1_su_degree, p1_mo_degree, p1_me_degree, p1_ma_degree, p1_ju_degree, p1_ve_degree, p1_sa_degree, p1_ra_degree, p1_ke_degree, p1_as_degree = request.POST['Su_Conc_p1'], request.POST['Mo_Conc_p1'], request.POST['Me_Conc_p1'], request.POST['Ma_Conc_p1'], request.POST['Ju_Conc_p1'], request.POST['Ve_Conc_p1'], request.POST['Sa_Conc_p1'], request.POST['Ra_Conc_p1'], request.POST['Ke_Conc_p1'], request.POST['As_Conc_p1']
        p2_su_degree, p2_mo_degree, p2_me_degree, p2_ma_degree, p2_ju_degree, p2_ve_degree, p2_sa_degree, p2_ra_degree, p2_ke_degree, p2_as_degree = request.POST['Su_Conc_p2'], request.POST['Mo_Conc_p2'], request.POST['Me_Conc_p2'], request.POST['Ma_Conc_p2'], request.POST['Ju_Conc_p2'], request.POST['Ve_Conc_p2'], request.POST['Sa_Conc_p2'], request.POST['Ra_Conc_p2'], request.POST['Ke_Conc_p2'], request.POST['As_Conc_p2']
        degree_dic["p1_su_degree"], degree_dic["p1_mo_degree"], degree_dic["p1_me_degree"], degree_dic["p1_ma_degree"], degree_dic["p1_ju_degree"], degree_dic["p1_ve_degree"], degree_dic["p1_sa_degree"], degree_dic["p1_ra_degree"], degree_dic["p1_ke_degree"], degree_dic["p1_as_degree"] = p1_su_degree, p1_mo_degree, p1_me_degree, p1_ma_degree, p1_ju_degree, p1_ve_degree, p1_sa_degree, p1_ra_degree, p1_ke_degree, p1_as_degree
        degree_dic["p2_su_degree"], degree_dic["p2_mo_degree"], degree_dic["p2_me_degree"], degree_dic["p2_ma_degree"], degree_dic["p2_ju_degree"], degree_dic["p2_ve_degree"], degree_dic["p2_sa_degree"], degree_dic["p2_ra_degree"], degree_dic["p2_ke_degree"], degree_dic["p2_as_degree"] = p2_su_degree, p2_mo_degree, p2_me_degree, p2_ma_degree, p2_ju_degree, p2_ve_degree, p2_sa_degree, p2_ra_degree, p2_ke_degree, p2_as_degree
        main_dic = p1vsp2_main(degree_dic["p1_su_degree"], degree_dic["p1_mo_degree"], degree_dic["p1_me_degree"], degree_dic["p1_ma_degree"], degree_dic["p1_ju_degree"], degree_dic["p1_ve_degree"], degree_dic["p1_sa_degree"], degree_dic["p1_ra_degree"], degree_dic["p1_ke_degree"], degree_dic["p1_as_degree"], degree_dic["p2_su_degree"], degree_dic["p2_mo_degree"], degree_dic["p2_me_degree"], degree_dic["p2_ma_degree"], degree_dic["p2_ju_degree"], degree_dic["p2_ve_degree"], degree_dic["p2_sa_degree"], degree_dic["p2_ra_degree"], degree_dic["p2_ke_degree"], degree_dic["p2_as_degree"])
        main_dic.update(degree_dic)
        return render(request, "p2p/p2phome.html", main_dic)
    return render(request, "p2p/p2phome.html", degree_dic)


def p1form(request):
    global degree_dic
    main_dic = p1main(degree_dic["p1_su_degree"], degree_dic["p1_mo_degree"], degree_dic["p1_me_degree"], degree_dic["p1_ma_degree"], degree_dic["p1_ju_degree"], degree_dic["p1_ve_degree"], degree_dic["p1_sa_degree"], degree_dic["p1_ra_degree"], degree_dic["p1_ke_degree"], degree_dic["p1_as_degree"])
    return render(request, "p2p/p1home.html", main_dic)


def p1xp2exactform(request):
    main_dic = p1xp2ex_main(degree_dic["p1_su_degree"], degree_dic["p1_mo_degree"], degree_dic["p1_me_degree"], degree_dic["p1_ma_degree"], degree_dic["p1_ju_degree"], degree_dic["p1_ve_degree"], degree_dic["p1_sa_degree"], degree_dic["p1_ra_degree"], degree_dic["p1_ke_degree"], degree_dic["p1_as_degree"], degree_dic["p2_su_degree"], degree_dic["p2_mo_degree"], degree_dic["p2_me_degree"], degree_dic["p2_ma_degree"], degree_dic["p2_ju_degree"], degree_dic["p2_ve_degree"], degree_dic["p2_sa_degree"], degree_dic["p2_ra_degree"], degree_dic["p2_ke_degree"], degree_dic["p2_as_degree"])
    return render(request, "p2p/p1xp2exacthome.html", main_dic)


def ax_report_form(request):
    if request.method == "POST":
        graph_planets = request.POST['g_planet']
        graph_degree = request.POST['g_degree']
        main_dic = graph_main(graph_planets, graph_degree)
        return render(request, "p2p/axhome.html", main_dic)
    return render(request, "p2p/axhome.html", {})


def dataframe_to_dict(df):
    json_records = df.reset_index().to_json(orient='records')
    data = []
    data = json.loads(json_records)
    return data

