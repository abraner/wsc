from django.urls import path
from . import views
from django.contrib.auth.views import LoginView


app_name = "wscdatabase"
urlpatterns = [
    path('wsc', LoginView.as_view(template_name='wsc/welcome.html'), name='wsc'),
    path('main/', views.main, name='main'),
    path('wsc/', views.welcome, name='wsc'),
    path('currentrm', views.currentrm, name='currentrm'),
    path('delete', views.delete, name='delete'),
    path('cust_info_existing', views.cust_info_existing, name='cust_info_existing'),
    path('con_info_existing', views.con_info_existing, name='con_info_existing'),
    path('newcon/', views.newcon, name='newcon'),
    path('<int:id>/dupconinfo/', views.dupconinfo, name='dupconinfo'),
    path('<int:id>/deletecust2/', views.deletecust2, name='deletecust2'),
    path('conerror', views.conerror, name='conerror'),
    path('custerror', views.custerror, name='custerror'),
    path('<int:id>/newcust/', views.newcust, name='newcust'),
    path('<int:id>/yesdupcon/', views.yesdupcon, name='yesdupcon'),
    path('<int:id>/addnewrm/', views.addnewrm, name='addnewrm'),
    path('deletecon/', views.deletecon, name='deletecon'),
    path('<int:id>/coninfo/', views.coninfo, name='coninfo'),
    path('<int:id>/custinfo/', views.custinfo, name='custinfo'),
    path('<int:id>/custinfo1/', views.custinfo1, name='custinfo1'),
    path('<int:id>/custinfo2/', views.custinfo2, name='custinfo2'),
    path('<int:id>/edit_cust_info/', views.edit_cust_info, name='edit_cust_info'),
    path('<int:id>/deletecust4/', views.deletecust4, name='deletecust4'),
    path('<int:id>/deletecust/', views.deletecust, name='deletecust'),
    path('<int:id>/deletecontractor/', views.deletecontractor, name='deletecontractor'),
    path('<int:id>/deletecon/', views.deletecon, name='deletecon'),
    path('<int:id>/prodqueue/', views.prodqueue, name='prodqueue'),

    path('<int:id>/load_rmcost1/', views.load_rmcost1, name='load_rmcost1'),
    path('<int:id>/load_rmcost2/', views.load_rmcost2, name='load_rmcost2'),
    path('<int:id>/load_rmcost3/', views.load_rmcost3, name='load_rmcost3'),
    path('<int:id>/load_rmcost4/', views.load_rmcost4, name='load_rmcost4'),
    path('<int:id>/load_rmcost5/', views.load_rmcost5, name='load_rmcost5'),
    path('<int:id>/load_rmcost6/', views.load_rmcost6, name='load_rmcost6'),
    path('<int:id>/load_rmcost7/', views.load_rmcost7, name='load_rmcost7'),
    path('<int:id>/load_rmcost8/', views.load_rmcost8, name='load_rmcost8'),
    path('<int:id>/load_rmcost9/', views.load_rmcost9, name='load_rmcost9'),
    path('<int:id>/load_rmcost10/', views.load_rmcost10, name='load_rmcost10'),
    path('<int:id>/load_rmcost11/', views.load_rmcost11, name='load_rmcost11'),
    path('<int:id>/load_rmcost12/', views.load_rmcost12, name='load_rmcost12'),
    path('<int:id>/load_rmcost13/', views.load_rmcost13, name='load_rmcost13'),

    path('<int:bid_idA>/appendcurrm/', views.appendcurrm, name='appendcurrm'),
    path('<int:id>/conedit/', views.conedit, name='conedit'),
    path('<int:id>/addnewcust/', views.addnewcust, name='addnewcust'),
    path('<int:id>/addcustconfirm/', views.addcustconfirm, name='addcustconfirm'),
    path('<int:id>/deletecustconfirm/', views.deletecustconfirm, name='deletecustconfirm'),
    path('<int:id>/deletecust3/', views.deletecust3, name='deletecust3'),
    path('<int:id>/addcust/', views.addcust, name='addcust'),

    path('<int:id>/viewnext/', views.viewnext, name='viewnext'),
    path('<int:id>/previouspage/', views.previouspage, name='previouspage'),
    path('<int:id>/bidpage/', views.bidpage, name='bidpage'),
    path('<int:id>/room/', views.room, name='room'),

    path('<int:id>/load_roomadd/', views.load_roomadd, name='load_roomadd'),

    path('<int:id>/rmmodal/', views.rmmodal, name='rmmodal'),

    path('<int:id>/cab1num/', views.cab1num, name='cab1num'),
    path('<int:id>/cab2num/', views.cab2num, name='cab2num'),
    path('<int:id>/cab3num/', views.cab3num, name='cab3num'),
    path('<int:idA>/cab4num/', views.cab4num, name='cab4num'),
    path('<int:idA>/cab5num/', views.cab5num, name='cab5num'),
    path('<int:idA>/cab6num/', views.cab6num, name='cab6num'),

    path('<int:id>/cab1/', views.cab1, name='cab1'),
    path('<int:id>/cab1A/', views.cab1A, name='cab1A'),
    path('<int:id>/deletecab1/', views.deletecab1, name='deletecab1'),

    path('<int:id>/cab2/', views.cab2, name='cab2'),
    path('<int:id>/cab2A/', views.cab2A, name='cab2A'),
    path('<int:id>/deletecab2/', views.deletecab2, name='deletecab2'),

    path('<int:id>/cab3/', views.cab3, name='cab3'),
    path('<int:id>/cab3A/', views.cab3A, name='cab3A'),
    path('<int:id>/deletecab3/', views.deletecab3, name='deletecab3'),

    path('<int:idA>/cab4/', views.cab4, name='cab4'),
    path('<int:idA>/cab4A/', views.cab4A, name='cab4A'),
    path('<int:idA>/deletecab4/', views.deletecab4, name='deletecab4'),

    path('<int:idA>/cab5/', views.cab5, name='cab5'),
    path('<int:idA>/cab5A/', views.cab5A, name='cab5A'),
    path('<int:idA>/deletecab5/', views.deletecab5, name='deletecab5'),

    path('<int:idA>/cab6/', views.cab6, name='cab6'),
    path('<int:idA>/cab6A/', views.cab6A, name='cab6A'),
    path('<int:idA>/deletecab6/', views.deletecab6, name='deletecab6'),

    path('<int:id>/cab1sides/', views.cab1sides, name='cab1sides'),
    path('<int:id>/cab1sidesA/', views.cab1sidesA, name='cab1sidesA'),

    path('<int:id>/cab2sides/', views.cab2sides, name='cab2sides'),
    path('<int:id>/cab2sidesA/', views.cab2sidesA, name='cab2sidesA'),

    path('<int:id>/cab3sides/', views.cab3sides, name='cab3sides'),
    path('<int:id>/cab3sidesA/', views.cab3sidesA, name='cab3sidesA'),

    path('<int:idA>/cab4sides/', views.cab4sides, name='cab4sides'),
    path('<int:idA>/cab4sidesA/', views.cab4sidesA, name='cab4sidesA'),

    path('<int:idA>/cab5sides/', views.cab5sides, name='cab5sides'),
    path('<int:idA>/cab5sidesA/', views.cab5sidesA, name='cab5sidesA'),

    path('<int:idA>/cab6sides/', views.cab6sides, name='cab6sides'),
    path('<int:idA>/cab6sidesA/', views.cab6sidesA, name='cab6sidesA'),

    path('<int:id>/drwer1/', views.drwer1, name='drwer1'),
    path('<int:id>/drwer1A/', views.drwer1A, name='drwer1A'),
    path('<int:id>/deletedrwer1/', views.deletedrwer1, name='deletedrwer1'),

    path('<int:id>/drwer2/', views.drwer2, name='drwer2'),
    path('<int:id>/drwer2A/', views.drwer2A, name='drwer2A'),
    path('<int:id>/deletedrwer2/', views.deletedrwer2, name='deletedrwer2'),

    path('<int:id>/drwer3/', views.drwer3, name='drwer3'),
    path('<int:id>/drwer3A/', views.drwer3A, name='drwer3A'),
    path('<int:id>/deletedrwer3/', views.deletedrwer3, name='deletedrwer3'),

    path('<int:idA>/drwer4/', views.drwer4, name='drwer4'),
    path('<int:idA>/drwer4A/', views.drwer4A, name='drwer4A'),
    path('<int:idA>/deletedrwer4/', views.deletedrwer4, name='deletedrwer4'),

    path('<int:idA>/drwer5/', views.drwer5, name='drwer5'),
    path('<int:idA>/drwer5A/', views.drwer5A, name='drwer5A'),
    path('<int:idA>/deletedrwer5/', views.deletedrwer5, name='deletedrwer5'),

    path('<int:idA>/drwer6/', views.drwer6, name='drwer6'),
    path('<int:idA>/drwer6A/', views.drwer6A, name='drwer6A'),
    path('<int:idA>/deletedrwer6/', views.deletedrwer6, name='deletedrwer6'),

    path('<int:id>/c11qty/', views.c11qty, name='c11qty'),
    path('<int:id>/c11qtyA/', views.c11qtyA, name='c11qtyA'),
    path('<int:id>/c12qty/', views.c12qty, name='c12qty'),
    path('<int:id>/c12qtyA/', views.c12qtyA, name='c12qtyA'),
    path('<int:id>/c13qty/', views.c13qty, name='c13qty'),
    path('<int:id>/c13qtyA/', views.c13qtyA, name='c13qtyA'),
    path('<int:id>/c14qty/', views.c14qty, name='c14qty'),
    path('<int:id>/c14qtyA/', views.c14qtyA, name='c14qtyA'),
    path('<int:id>/c15qty/', views.c15qty, name='c15qty'),
    path('<int:id>/c15qtyA/', views.c15qtyA, name='c15qtyA'),

    path('<int:id>/c21qty/', views.c21qty, name='c21qty'),
    path('<int:id>/c21qtyA/', views.c21qtyA, name='c21qtyA'),
    path('<int:id>/c22qty/', views.c22qty, name='c22qty'),
    path('<int:id>/c22qtyA/', views.c22qtyA, name='c22qtyA'),
    path('<int:id>/c23qty/', views.c23qty, name='c23qty'),
    path('<int:id>/c23qtyA/', views.c23qtyA, name='c23qtyA'),
    path('<int:id>/c24qty/', views.c24qty, name='c24qty'),
    path('<int:id>/c24qtyA/', views.c24qtyA, name='c24qtyA'),
    path('<int:id>/c25qty/', views.c25qty, name='c25qty'),
    path('<int:id>/c25qtyA/', views.c25qtyA, name='c25qtyA'),

    path('<int:id>/c31qty/', views.c31qty, name='c31qty'),
    path('<int:id>/c31qtyA/', views.c31qtyA, name='c31qtyA'),
    path('<int:id>/c32qty/', views.c32qty, name='c32qty'),
    path('<int:id>/c32qtyA/', views.c32qtyA, name='c32qtyA'),
    path('<int:id>/c33qty/', views.c33qty, name='c33qty'),
    path('<int:id>/c33qtyA/', views.c33qtyA, name='c33qtyA'),
    path('<int:id>/c34qty/', views.c34qty, name='c34qty'),
    path('<int:id>/c34qtyA/', views.c34qtyA, name='c34qtyA'),
    path('<int:id>/c35qty/', views.c35qty, name='c35qty'),
    path('<int:id>/c35qtyA/', views.c35qtyA, name='c35qtyA'),

    path('<int:idA>/c41qty/', views.c41qty, name='c41qty'),
    path('<int:idA>/c41qtyA/', views.c41qtyA, name='c41qtyA'),
    path('<int:idA>/c42qty/', views.c42qty, name='c42qty'),
    path('<int:idA>/c42qtyA/', views.c42qtyA, name='c42qtyA'),
    path('<int:idA>/c43qty/', views.c43qty, name='c43qty'),
    path('<int:idA>/c43qtyA/', views.c43qtyA, name='c43qtyA'),
    path('<int:idA>/c44qty/', views.c44qty, name='c44qty'),
    path('<int:idA>/c44qtyA/', views.c44qtyA, name='c44qtyA'),
    path('<int:idA>/c45qty/', views.c45qty, name='c45qty'),
    path('<int:idA>/c45qtyA/', views.c45qtyA, name='c45qtyA'),

    path('<int:idA>/c51qty/', views.c51qty, name='c51qty'),
    path('<int:idA>/c51qtyA/', views.c51qtyA, name='c51qtyA'),
    path('<int:idA>/c52qty/', views.c52qty, name='c52qty'),
    path('<int:idA>/c52qtyA/', views.c52qtyA, name='c52qtyA'),
    path('<int:idA>/c53qty/', views.c53qty, name='c53qty'),
    path('<int:idA>/c53qtyA/', views.c53qtyA, name='c53qtyA'),
    path('<int:idA>/c54qty/', views.c54qty, name='c54qty'),
    path('<int:idA>/c54qtyA/', views.c54qtyA, name='c54qtyA'),
    path('<int:idA>/c55qty/', views.c55qty, name='c55qty'),
    path('<int:idA>/c55qtyA/', views.c55qtyA, name='c55qtyA'),

    path('<int:idA>/c61qty/', views.c61qty, name='c61qty'),
    path('<int:idA>/c61qtyA/', views.c61qtyA, name='c61qtyA'),
    path('<int:idA>/c62qty/', views.c62qty, name='c62qty'),
    path('<int:idA>/c62qtyA/', views.c62qtyA, name='c62qtyA'),
    path('<int:idA>/c63qty/', views.c63qty, name='c63qty'),
    path('<int:idA>/c63qtyA/', views.c63qtyA, name='c63qtyA'),
    path('<int:idA>/c64qty/', views.c64qty, name='c64qty'),
    path('<int:idA>/c64qtyA/', views.c64qtyA, name='c64qtyA'),
    path('<int:idA>/c65qty/', views.c65qty, name='c65qty'),
    path('<int:idA>/c65qtyA/', views.c65qtyA, name='c65qtyA'),

    path('<int:id>/comp11/', views.comp11, name='comp11'),
    path('<int:id>/comp11A/', views.comp11A, name='comp11A'),
    path('<int:id>/deletecomp11/', views.deletecomp11, name='deletecomp11'),
    path('<int:id>/deletecomp11A/', views.deletecomp11A, name='deletecomp11A'),
    path('<int:id>/comp12/', views.comp12, name='comp12'),
    path('<int:id>/comp12A/', views.comp12A, name='comp12A'),
    path('<int:id>/deletecomp12/', views.deletecomp12, name='deletecomp12'),
    path('<int:id>/deletecomp12A/', views.deletecomp12A, name='deletecomp12A'),
    path('<int:id>/comp13/', views.comp13, name='comp13'),
    path('<int:id>/comp13A/', views.comp13A, name='comp13A'),
    path('<int:id>/deletecomp13/', views.deletecomp13, name='deletecomp13'),
    path('<int:id>/deletecomp13A/', views.deletecomp13A, name='deletecomp13A'),
    path('<int:id>/comp14/', views.comp14, name='comp14'),
    path('<int:id>/comp14A/', views.comp14A, name='comp14A'),
    path('<int:id>/deletecomp14/', views.deletecomp14, name='deletecomp14'),
    path('<int:id>/deletecomp14A/', views.deletecomp14A, name='deletecomp14A'),
    path('<int:id>/comp15/', views.comp15, name='comp15'),
    path('<int:id>/comp15A/', views.comp15A, name='comp15A'),
    path('<int:id>/deletecomp15/', views.deletecomp15, name='deletecomp15'),
    path('<int:id>/deletecomp15A/', views.deletecomp15A, name='deletecomp15A'),

    path('<int:id>/comp21/', views.comp21, name='comp21'),
    path('<int:id>/comp21A/', views.comp21A, name='comp21A'),
    path('<int:id>/deletecomp21/', views.deletecomp21, name='deletecomp21'),
    path('<int:id>/deletecomp21A/', views.deletecomp21A, name='deletecomp21A'),
    path('<int:id>/comp22/', views.comp22, name='comp22'),
    path('<int:id>/comp22A/', views.comp22A, name='comp22A'),
    path('<int:id>/deletecomp22/', views.deletecomp22, name='deletecomp22'),
    path('<int:id>/deletecomp22A/', views.deletecomp22A, name='deletecomp22A'),
    path('<int:id>/comp23/', views.comp23, name='comp23'),
    path('<int:id>/comp23A/', views.comp23A, name='comp23A'),
    path('<int:id>/deletecomp23/', views.deletecomp23, name='deletecomp23'),
    path('<int:id>/deletecomp23A/', views.deletecomp23A, name='deletecomp23A'),
    path('<int:id>/comp24/', views.comp24, name='comp24'),
    path('<int:id>/comp24A/', views.comp24A, name='comp24A'),
    path('<int:id>/deletecomp24/', views.deletecomp24, name='deletecomp24'),
    path('<int:id>/deletecomp24A/', views.deletecomp24A, name='deletecomp24A'),
    path('<int:id>/comp25/', views.comp25, name='comp25'),
    path('<int:id>/comp25A/', views.comp25A, name='comp25A'),
    path('<int:id>/deletecomp25/', views.deletecomp25, name='deletecomp25'),
    path('<int:id>/deletecomp25A/', views.deletecomp25A, name='deletecomp25A'),

    path('<int:id>/comp31/', views.comp31, name='comp31'),
    path('<int:id>/comp31A/', views.comp31A, name='comp31A'),
    path('<int:id>/deletecomp31/', views.deletecomp31, name='deletecomp31'),
    path('<int:id>/deletecomp31A/', views.deletecomp31A, name='deletecomp31A'),
    path('<int:id>/comp32/', views.comp32, name='comp32'),
    path('<int:id>/comp32A/', views.comp32A, name='comp32A'),
    path('<int:id>/deletecomp32/', views.deletecomp32, name='deletecomp32'),
    path('<int:id>/deletecomp32A/', views.deletecomp32A, name='deletecomp32A'),
    path('<int:id>/comp33/', views.comp33, name='comp33'),
    path('<int:id>/comp33A/', views.comp33A, name='comp33A'),
    path('<int:id>/deletecomp33/', views.deletecomp33, name='deletecomp33'),
    path('<int:id>/deletecomp33A/', views.deletecomp33A, name='deletecomp33A'),
    path('<int:id>/comp34/', views.comp34, name='comp34'),
    path('<int:id>/comp34A/', views.comp34A, name='comp34A'),
    path('<int:id>/deletecomp34/', views.deletecomp34, name='deletecomp34'),
    path('<int:id>/deletecomp34A/', views.deletecomp34A, name='deletecomp34A'),
    path('<int:id>/comp35/', views.comp35, name='comp35'),
    path('<int:id>/comp35A/', views.comp35A, name='comp35A'),
    path('<int:id>/deletecomp35/', views.deletecomp35, name='deletecomp35'),
    path('<int:id>/deletecomp35A/', views.deletecomp35A, name='deletecomp35A'),

    path('<int:idA>/comp41/', views.comp41, name='comp41'),
    path('<int:idA>/comp41A/', views.comp41A, name='comp41A'),
    path('<int:idA>/deletecomp41/', views.deletecomp41, name='deletecomp41'),
    path('<int:idA>/deletecomp41A/', views.deletecomp41A, name='deletecomp41A'),
    path('<int:idA>/comp42/', views.comp42, name='comp42'),
    path('<int:idA>/comp42A/', views.comp42A, name='comp42A'),
    path('<int:idA>/deletecomp42/', views.deletecomp42, name='deletecomp42'),
    path('<int:idA>/deletecomp42A/', views.deletecomp42A, name='deletecomp42A'),
    path('<int:idA>/comp43/', views.comp43, name='comp43'),
    path('<int:idA>/comp43A/', views.comp43A, name='comp43A'),
    path('<int:idA>/deletecomp43/', views.deletecomp43, name='deletecomp43'),
    path('<int:idA>/deletecomp43A/', views.deletecomp43A, name='deletecomp43A'),
    path('<int:idA>/comp44/', views.comp44, name='comp44'),
    path('<int:idA>/comp44A/', views.comp44A, name='comp44A'),
    path('<int:idA>/deletecomp44/', views.deletecomp44, name='deletecomp44'),
    path('<int:idA>/deletecomp44A/', views.deletecomp44A, name='deletecomp44A'),
    path('<int:idA>/comp45/', views.comp45, name='comp45'),
    path('<int:idA>/comp45A/', views.comp45A, name='comp45A'),
    path('<int:idA>/deletecomp45/', views.deletecomp45, name='deletecomp45'),
    path('<int:idA>/deletecomp45A/', views.deletecomp45A, name='deletecomp45A'),

    path('<int:idA>/comp51/', views.comp51, name='comp51'),
    path('<int:idA>/comp51A/', views.comp51A, name='comp51A'),
    path('<int:idA>/deletecomp51/', views.deletecomp51, name='deletecomp51'),
    path('<int:idA>/deletecomp51A/', views.deletecomp51A, name='deletecomp51A'),
    path('<int:idA>/comp52/', views.comp52, name='comp52'),
    path('<int:idA>/comp52A/', views.comp52A, name='comp52A'),
    path('<int:idA>/deletecomp52/', views.deletecomp52, name='deletecomp52'),
    path('<int:idA>/deletecomp52A/', views.deletecomp52A, name='deletecomp52A'),
    path('<int:idA>/comp53/', views.comp53, name='comp53'),
    path('<int:idA>/comp53A/', views.comp53A, name='comp53A'),
    path('<int:idA>/deletecomp53/', views.deletecomp53, name='deletecomp53'),
    path('<int:idA>/deletecomp53A/', views.deletecomp53A, name='deletecomp53A'),
    path('<int:idA>/comp54/', views.comp54, name='comp54'),
    path('<int:idA>/comp54A/', views.comp54A, name='comp54A'),
    path('<int:idA>/deletecomp54/', views.deletecomp54, name='deletecomp54'),
    path('<int:idA>/deletecomp54A/', views.deletecomp54A, name='deletecomp54A'),
    path('<int:idA>/comp55/', views.comp55, name='comp55'),
    path('<int:idA>/comp55A/', views.comp55A, name='comp55A'),
    path('<int:idA>/deletecomp55/', views.deletecomp55, name='deletecomp55'),
    path('<int:idA>/deletecomp55A/', views.deletecomp55A, name='deletecomp55A'),

    path('<int:idA>/comp61/', views.comp61, name='comp61'),
    path('<int:idA>/comp61A/', views.comp61A, name='comp61A'),
    path('<int:idA>/deletecomp61/', views.deletecomp61, name='deletecomp61'),
    path('<int:idA>/deletecomp61A/', views.deletecomp61A, name='deletecomp61A'),
    path('<int:idA>/comp62/', views.comp62, name='comp62'),
    path('<int:idA>/comp62A/', views.comp62A, name='comp62A'),
    path('<int:idA>/deletecomp62/', views.deletecomp62, name='deletecomp62'),
    path('<int:idA>/deletecomp62A/', views.deletecomp62A, name='deletecomp62A'),
    path('<int:idA>/comp63/', views.comp63, name='comp63'),
    path('<int:idA>/comp63A/', views.comp63A, name='comp63A'),
    path('<int:idA>/deletecomp63/', views.deletecomp63, name='deletecomp63'),
    path('<int:idA>/deletecomp63A/', views.deletecomp63A, name='deletecomp63A'),
    path('<int:idA>/comp64/', views.comp64, name='comp64'),
    path('<int:idA>/comp64A/', views.comp64A, name='comp64A'),
    path('<int:idA>/deletecomp64/', views.deletecomp64, name='deletecomp64'),
    path('<int:idA>/deletecomp64A/', views.deletecomp64A, name='deletecomp64A'),
    path('<int:idA>/comp65/', views.comp65, name='comp65'),
    path('<int:idA>/comp65A/', views.comp65A, name='comp65A'),
    path('<int:idA>/deletecomp65/', views.deletecomp65, name='deletecomp65'),
    path('<int:idA>/deletecomp65A/', views.deletecomp65A, name='deletecomp65A'),

    path('<int:id>/newbidpage/', views.newbidpage, name='newbidpage'),
    path('<int:bid_idA>/changermnum/', views.changermnum, name='changermnum'),
    path('<int:bid_idA>/totalrmcost/', views.totalrmcost, name='totalrmcost'),
    path('<int:bid_idA>/totalrmcost2/', views.totalrmcost2, name='totalrmcost2'),
    path('<int:id>/totalrmcost3/', views.totalrmcost3, name='totalrmcost3'),

    path('<int:bid_idA>/woodspecies/', views.woodspecies, name='woodspecies'),
    path('<int:bid_idA>/load_woodspecies/', views.load_woodspecies, name='load_woodspecies'),
    path('<int:bid_idA>/load_woodspeciesperc/', views.load_woodspeciesperc, name='load_woodspeciesperc'),

    path('<int:bid_idA>/doorstyle/', views.doorstyle, name='doorstyle'),
    path('<int:bid_idA>/load_doorstyle/', views.load_doorstyle, name='load_doorstyle'),
    path('<int:bid_idA>/load_doorstyleperc/', views.load_doorstyleperc, name='load_doorstyleperc'),

    path('<int:bid_idA>/finishcolor/', views.finishcolor, name='finishcolor'),
    path('<int:bid_idA>/load_finishcolor/', views.load_finishcolor, name='load_finishcolor'),
    path('<int:bid_idA>/load_finishcolorperc/', views.load_finishcolorperc, name='load_finishcolorperc'),

    path('<int:bid_idA>/finishoption/', views.finishoption, name='finishoption'),
    path('<int:bid_idA>/load_finishoption/', views.load_finishoption, name='load_finishoption'),
    path('<int:bid_idA>/load_finishoptionperc/', views.load_finishoptionperc, name='load_finishoptionperc'),
    path('<int:bid_idA>/finishoption2/', views.finishoption2, name='finishoption2'),
    path('<int:bid_idA>/load_finishoption2/', views.load_finishoption2, name='load_finishoption2'),
    path('<int:bid_idA>/load_finishoptionperc2/', views.load_finishoptionperc2, name='load_finishoptionperc2'),


    path('<int:bid_idA>/load_totalperc/', views.load_totalperc, name='load_totalperc'),


    path('<int:bid_idA>/load_cabinet/', views.load_cabinet, name='load_cabinet'),
    path('<int:bid_idA>/load_cabinet2/', views.load_cabinet2, name='load_cabinet2'),

    path('<int:id>/addnewrm/', views.addnewrm, name='addnewrm'),
    path('<int:id>/addrm1/', views.addrm1, name='addrm1'),
    path('<int:id>/ajax/load_room/', views.load_room, name='ajax_load_room'),

    path('<int:id>/addnewrm2/', views.addnewrm2, name='addnewrm2'),
    path('<int:bid_idA>/updatetotalrmcost/', views.updatetotalrmcost, name='updatetotalrmcost'),

    path('<int:bid_id>/openbidpage/', views.openbidpage, name='openbidpage'),

    path('<int:bid_idA>/rmselection/', views.rmselection, name='rmselection'),
    path('<int:id>/bidpageselection/', views.bidpageselection, name='bidpageselection'),
    path('<int:bid_idA>/addtocontract/', views.addtocontract, name='addtocontract'),
    path('<int:bid_idA>/yescontract/', views.yescontract, name='yescontract'),
    path('<int:bid_idA>/nocontract/', views.nocontract, name='nocontract'),
    path('<int:bid_idA>/deleterm1/', views.deleterm1, name='deleterm1'),
    path('<int:bid_idA>/deleterm/', views.deleterm, name='deleterm'),
    path('<int:bid_idA>/deleterm2/', views.deleterm2, name='deleterm2'),
    path('<int:bid_idA>/existingrm/', views.existingrm, name='existingrm'),


    path('deletermtable', views.deletermtable, name='deletermtable'),

    path('rmerror', views.rmerror, name='rmerror'),
    path('red', views.red, name='red'),

    path('<int:id>/jobcost/', views.jobcost, name='jobcost'),

    path('<int:custid>/load_subtotalcost/', views.load_subtotalcost, name='load_subtotalcost'),
    path('<int:custid>/tax/', views.tax, name='tax'),
    path('<int:custid>/load_tax/', views.load_tax, name='load_tax'),
    path('<int:custid>/load_totaljobcost/', views.load_totaljobcost, name='load_totaljobcost'),
    path('<int:custid>/load_grandtotalcost/', views.load_grandtotalcost, name='load_grandtotalcost'),

    path('<int:custid>/load_customtext/', views.load_customtext, name='load_customtext'),
    path('<int:custid>/customtext/', views.customtext, name='customtext'),
    path('<int:custid>/custom/', views.custom, name='custom'),
    path('<int:custid>/custom1/', views.custom1, name='custom1'),
    path('<int:custid>/load_custom/', views.load_custom, name='load_custom'),

    path('<int:custid>/load_discounttext/', views.load_discounttext, name='load_discounttext'),
    path('<int:custid>/discounttext/', views.discounttext, name='discounttext'),
    path('<int:custid>/discount/', views.discount, name='discount'),
    path('<int:custid>/load_discount/', views.load_discount, name='load_discount'),

    path('<int:custid>/load_constructiontext/', views.load_constructiontext, name='load_constructiontext'),
    path('<int:custid>/constructiontext/', views.constructiontext, name='constructiontext'),
    path('<int:custid>/construction/', views.construction, name='construction'),
    path('<int:custid>/load_construction/', views.load_construction, name='load_construction'),

    path('<int:custid>/load_opt2text/', views.load_opt2text, name='load_opt2text'),
    path('<int:custid>/opt2text/', views.opt2text, name='opt2text'),
    path('<int:custid>/opt2/', views.opt2, name='opt2'),
    path('<int:custid>/load_opt2/', views.load_opt2, name='load_opt2'),

    path('<int:custid>/load_opt3text/', views.load_opt3text, name='load_opt3text'),
    path('<int:custid>/opt3text/', views.opt3text, name='opt3text'),
    path('<int:custid>/opt3/', views.opt3, name='opt3'),
    path('<int:custid>/load_opt3/', views.load_opt3, name='load_opt3'),

    path('<int:custid>/load_install/', views.load_install, name='load_install'),

    path('<int:custid>/load_installtext/', views.load_installtext, name='load_installtext'),
    path('<int:custid>/installtext/', views.installtext, name='installtext'),
    path('<int:custid>/installyes/', views.installyes, name='installyes'),
    path('<int:custid>/installno/', views.installno, name='installno'),
    path('<int:custid>/load_installrate/', views.load_installrate, name='load_installrate'),

    path('<int:custid>/totallabor/', views.totallabor, name='totallabor'),
    path('<int:custid>/laborbd/', views.laborbd, name='laborbd'),
    path('<int:custid>/laborbd2/', views.laborbd2, name='laborbd2'),
    path('<int:custid>/laborbd3/', views.laborbd3, name='laborbd3'),

    path('<int:custid>/contract/', views.contract, name='contract'),
    path('<int:custid>/workorderdate/', views.workorderdate, name='workorderdate'),
    path('<int:custid>/load_workorderdate/', views.load_workorderdate, name='load_workorderdate'),
    path('<int:custid>/memo1/', views.memo1, name='memo1'),
    path('<int:custid>/load_memo1/', views.load_memo1, name='load_memo1'),
    path('<int:custid>/worktype/', views.worktype, name='worktype'),
    path('<int:custid>/load_worktype/', views.load_worktype, name='load_worktype'),
    path('<int:custid>/memo2/', views.memo2, name='memo2'),
    path('<int:custid>/load_memo2/', views.load_memo2, name='load_memo2'),
    path('<int:custid>/memo3/', views.memo3, name='memo3'),
    path('<int:custid>/load_memo3/', views.load_memo3, name='load_memo3'),
    path('<int:custid>/memo4/', views.memo4, name='memo4'),
    path('<int:custid>/load_memo4/', views.load_memo4, name='load_memo4'),
    path('<int:custid>/memo5/', views.memo5, name='memo5'),
    path('<int:custid>/load_memo5/', views.load_memo5, name='load_memo5'),
    path('<int:custid>/memo6/', views.memo6, name='memo6'),
    path('<int:custid>/load_memo6/', views.load_memo6, name='load_memo6'),
    path('<int:custid>/memo7/', views.memo7, name='memo7'),
    path('<int:custid>/load_memo7/', views.load_memo7, name='load_memo7'),
    path('<int:custid>/memo8/', views.memo8, name='memo8'),
    path('<int:custid>/load_memo8/', views.load_memo8, name='load_memo8'),
    path('<int:custid>/memo9/', views.memo9, name='memo9'),
    path('<int:custid>/load_memo9/', views.load_memo9, name='load_memo9'),
    path('<int:custid>/memo10/', views.memo10, name='memo10'),
    path('<int:custid>/load_memo10/', views.load_memo10, name='load_memo10'),
    path('<int:custid>/memo11/', views.memo11, name='memo11'),
    path('<int:custid>/load_memo11/', views.load_memo11, name='load_memo11'),
    path('<int:custid>/memo12/', views.memo12, name='memo12'),
    path('<int:custid>/load_memo12/', views.load_memo12, name='load_memo12'),
    path('<int:custid>/memo13/', views.memo13, name='memo13'),
    path('<int:custid>/load_memo13/', views.load_memo13, name='load_memo13'),
    path('<int:custid>/memo14/', views.memo14, name='memo14'),
    path('<int:custid>/load_memo14/', views.load_memo14, name='load_memo14'),
    path('<int:custid>/memo15/', views.memo15, name='memo15'),
    path('<int:custid>/load_memo15/', views.load_memo15, name='load_memo15'),
    path('<int:custid>/memo16/', views.memo16, name='memo16'),
    path('<int:custid>/load_memo16/', views.load_memo16, name='load_memo16'),
    path('<int:custid>/memo17/', views.memo17, name='memo17'),
    path('<int:custid>/load_memo17/', views.load_memo17, name='load_memo17'),
    path('<int:custid>/depositperc/', views.depositperc, name='depositperc'),
    path('<int:custid>/load_depositperc/', views.load_depositperc, name='load_depositperc'),
    path('<int:custid>/payment2perc/', views.payment2perc, name='payment2perc'),
    path('<int:custid>/load_payment2perc/', views.load_payment2perc, name='load_payment2perc'),
    path('<int:custid>/payment3perc/', views.payment3perc, name='payment3perc'),
    path('<int:custid>/load_payment3perc/', views.load_payment3perc, name='load_payment3perc'),
    path('<int:custid>/payment4perc/', views.payment4perc, name='payment4perc'),
    path('<int:custid>/load_payment4perc/', views.load_payment4perc, name='load_payment4perc'),
    path('<int:custid>/depositterms/', views.depositterms, name='depositterms'),
    path('<int:custid>/load_depositterms/', views.load_depositterms, name='load_depositterms'),
    path('<int:custid>/terms2/', views.terms2, name='terms2'),
    path('<int:custid>/load_terms2/', views.load_terms2, name='load_terms2'),
    path('<int:custid>/terms3/', views.terms3, name='terms3'),
    path('<int:custid>/load_terms3/', views.load_terms3, name='load_terms3'),
    path('<int:custid>/terms4/', views.terms4, name='terms4'),
    path('<int:custid>/load_terms4/', views.load_terms4, name='load_terms4'),
    path('<int:custid>/termsfinal/', views.termsfinal, name='termsfinal'),
    path('<int:custid>/load_termsfinal/', views.load_termsfinal, name='load_termsfinal'),
    path('<int:custid>/load_depositamount/', views.load_depositamount, name='load_depositamount'),

    path('<int:custid>/load_finalpayment/', views.load_finalpayment, name='load_finalpayment'),
    path('<int:custid>/customdeposit/', views.customdeposit, name='customdeposit'),
    path('<int:custid>/cdp/', views.cdp, name='cdp'),
    path('<int:custid>/load_secondamount/', views.load_secondamount, name='load_secondamount'),
    path('<int:custid>/seconddeposit/', views.seconddeposit, name='seconddeposit'),
    path('<int:custid>/secdp/', views.secdp, name='secdp'),
    path('<int:custid>/load_thirdamount/', views.load_thirdamount, name='load_thirdamount'),
    path('<int:custid>/thirddeposit/', views.thirddeposit, name='thirddeposit'),
    path('<int:custid>/thirddp/', views.thirddp, name='thirddp'),
    path('<int:custid>/load_forthamount/', views.load_forthamount, name='load_forthamount'),
    path('<int:custid>/forthdeposit/', views.forthdeposit, name='forthdeposit'),
    path('<int:custid>/forthdp/', views.forthdp, name='forthdp'),
    path('<int:custid>/depositdate/', views.depositdate, name='depositdate'),
    path('<int:custid>/load_depositdate/', views.load_depositdate, name='load_depositdate'),
    path('<int:custid>/depositdate/', views.depositdate, name='depositdate'),
    path('<int:custid>/load_depositdate/', views.load_depositdate, name='load_depositdate'),
    path('<int:custid>/payment2date/', views.payment2date, name='payment2date'),
    path('<int:custid>/load_payment2date/', views.load_payment2date, name='load_payment2date'),
    path('<int:custid>/payment3date/', views.payment3date, name='payment3date'),
    path('<int:custid>/load_payment3date/', views.load_payment3date, name='load_payment3date'),
    path('<int:custid>/payment4date/', views.payment4date, name='payment4date'),
    path('<int:custid>/load_payment4date/', views.load_payment4date, name='load_payment4date'),
    path('<int:custid>/finalpaymentdate/', views.finalpaymentdate, name='finalpaymentdate'),
    path('<int:custid>/load_finalpaymentdate/', views.load_finalpaymentdate, name='load_finalpaymentdate'),

    path('<int:custid>/installrate/', views.installrate, name='installrate'),
    path('<int:custid>/agreementlist/', views.agreementlist, name='agreementlist'),
    path('<int:custid>/worktypelistdescr/', views.worktypelistdescr, name='worktypelistdescr'),
    path('<int:custid>/worktypedescr/', views.worktypedescr, name='worktypedescr'),
    path('<int:custid>/includedescr/', views.includedescr, name='includedescr'),
    path('<int:custid>/excludedescr/', views.excludedescr, name='excludedescr'),

]

