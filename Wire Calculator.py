'''Boeing 737 Wire Length Calculator tool
This software is not affliated with The Boeing Aircraft Company.
creator: openthird3ye
REV_  01/31/2024
'''

import math
import tkinter
from tkinter import *
from ttkbootstrap.constants import *
from tkinter import messagebox, ttk
import ttkbootstrap as ttkb

valueStafwd = 0
valueStaaft = 0
xsta = 0
ysta = 0
xstr = 0
ystr = 0
xbl = 0
ybl = 0


def selection_acfttype(event):
    selectionType = acfttypeDp.get()
    print("Aircraft Selected ", selectionType)
#    messagebox.showinfo(
#        title="Aircraft Type",
#        message=f"Selection: {selectionType}"
#    )


def selection_changedfwd(event):
    selectionfwd = stafwd.get()
    print("STA FWD: ", selectionfwd)
#    messagebox.showinfo(
#        title="Check FWD",
#        message=f"Selection: {selectionfwd}"
#    )


def selection_changedaft(event):
    selectionaft = staaft.get()
    print("STA AFT: ", selectionaft)
#    messagebox.showinfo(
#        title="Check AFT",
#        message=f"Selection: {selectionaft}"

#    )


def selection_strStart(event):
    selectionstrStart = strStart.get()
    print("STR Start: ", selectionstrStart)
#    messagebox.showinfo(
#        title="BL",
#        message=f"Selection: {selectionstrStart}"

#    )


def selection_strEnd(event):
    selectionstrEnd = strEnd.get()
    print("STR AFT: ", selectionstrEnd)
#    messagebox.showinfo(
#        title="BL",
#        message=f"Selection: {selectionstrEnd}"

#    )


def submitButton():
    valueAcftType = acfttypeDp.get()
    valueStafwd = stafwd.get()
    valueStaaft = staaft.get()
    valueStrStart = strStart.get()
    valueStrEnd = strEnd.get()
#    valuewlSliderStart = int(wlSliderStart.get())
#    valueSliderEnd = int(wlSliderEnd.get())
    valueOverage = int(overPercent.get())
    crossVar = cross.get()
    valueBlStart = BlStart.get()
    valueBlEnd = BlEnd.get()

#    print(valueAcftType, valueStaaft, valueStafwd, valueStrEnd, valueStrStart, valueBlEnd, valuewlSliderStart,
#          valueSliderEnd, valueOverage, crossVar, valueBlStart)

# 737-700 and FWD Sta Value
    if (valueAcftType == "737-700") and (valueStafwd == "130"):
        xsta = 130
    elif (valueAcftType == "737-700") and (valueStafwd == "178"):
        xsta = 178
    elif (valueAcftType == "737-700") and (valueStafwd == "259.5"):
        xsta = 259.9
    elif (valueAcftType == "737-700") and (valueStafwd == "360"):
        xsta = 360
    elif (valueAcftType == "737-700") and (valueStafwd == "380"):
        xsta = 380
    elif (valueAcftType == "737-700") and (valueStafwd == "400"):
        xsta = 400
    elif (valueAcftType == "737-700") and (valueStafwd == "420"):
        xsta = 420
    elif (valueAcftType == "737-700") and (valueStafwd == "440"):
        xsta = 440
    elif (valueAcftType == "737-700") and (valueStafwd == "460"):
        xsta = 460
    elif (valueAcftType == "737-700") and (valueStafwd == "480"):
        xsta = 480
    elif (valueAcftType == "737-700") and (valueStafwd == "500"):
        xsta = 500
    elif (valueAcftType == "737-700") and (valueStafwd == "500A"):
        xsta = 520
    elif (valueAcftType == "737-700") and (valueStafwd == "500B"):
        xsta = 540
    elif (valueAcftType == "737-700") and (valueStafwd == "500C"):
        xsta = 560
    elif (valueAcftType == "737-700") and (valueStafwd == "500D"):
        xsta = 580
    elif (valueAcftType == "737-700") and (valueStafwd == "500E"):
        xsta = 0
    elif (valueAcftType == "737-700") and (valueStafwd == "500F"):
        xsta = 0
    elif (valueAcftType == "737-700") and (valueStafwd == "500G"):
        xsta = 0
    elif (valueAcftType == "737-700") and (valueStafwd == "500H"):
        xsta = 0
    elif (valueAcftType == "737-700") and (valueStafwd == "500I"):
        xsta = 0
    elif (valueAcftType == "737-700") and (valueStafwd == "500J"):
        xsta = 0
    elif (valueAcftType == "737-700") and (valueStafwd == "500K"):
        xsta = 0
    elif (valueAcftType == "737-700") and (valueStafwd == "500L"):
        xsta = 0
    elif (valueAcftType == "737-700") and (valueStafwd == "520"):
        xsta = 600
    elif (valueAcftType == "737-700") and (valueStafwd == "540"):
        xsta = 620
    elif (valueAcftType == "737-700") and (valueStafwd == "559"):
        xsta = 639
    elif (valueAcftType == "737-700") and (valueStafwd == "578"):
        xsta = 658
    elif (valueAcftType == "737-700") and (valueStafwd == "597"):
        xsta = 676
    elif (valueAcftType == "737-700") and (valueStafwd == "616"):
        xsta = 696
    elif (valueAcftType == "737-700") and (valueStafwd == "639"):
        xsta = 719
    elif (valueAcftType == "737-700") and (valueStafwd == "663.75"):
        xsta = 743.5
    elif (valueAcftType == "737-700") and (valueStafwd == "685"):
        xsta = 765
    elif (valueAcftType == "737-700") and (valueStafwd == "706"):
        xsta = 786
    elif (valueAcftType == "737-700") and (valueStafwd == "727"):
        xsta = 807
    elif (valueAcftType == "737-700") and (valueStafwd == "727A"):
        xsta = 827
    elif (valueAcftType == "737-700") and (valueStafwd == "727B"):
        xsta = 847
    elif (valueAcftType == "737-700") and (valueStafwd == "727C"):
        xsta = 867
    elif (valueAcftType == "737-700") and (valueStafwd == "727D"):
        xsta = 887
    elif (valueAcftType == "737-700") and (valueStafwd == "727E"):
        xsta = 0
    elif (valueAcftType == "737-700") and (valueStafwd == "727F"):
        xsta = 0
    elif (valueAcftType == "737-700") and (valueStafwd == "727G"):
        xsta = 0
    elif (valueAcftType == "737-700") and (valueStafwd == "727H"):
        xsta = 0
    elif (valueAcftType == "737-700") and (valueStafwd == "727G"):
        xsta = 0
    elif (valueAcftType == "737-700") and (valueStafwd == "727H"):
        xsta = 0
    elif (valueAcftType == "737-700") and (valueStafwd == "727I"):
        xsta = 0
    elif (valueAcftType == "737-700") and (valueStafwd == "727J"):
        xsta = 0
    elif (valueAcftType == "737-700") and (valueStafwd == "727K"):
        xsta = 0
    elif (valueAcftType == "737-700") and (valueStafwd == "727J"):
        xsta = 0
    elif (valueAcftType == "737-700") and (valueStafwd == "727L"):
        xsta = 0
    elif (valueAcftType == "737-700") and (valueStafwd == "747"):
        xsta = 927
    elif (valueAcftType == "737-700") and (valueStafwd == "767"):
        xsta = 947
    elif (valueAcftType == "737-700") and (valueStafwd == "787"):
        xsta = 967
    elif (valueAcftType == "737-700") and (valueStafwd == "807"):
        xsta = 987
    elif (valueAcftType == "737-700") and (valueStafwd == "827"):
        xsta = 1007
    elif (valueAcftType == "737-700") and (valueStafwd == "847"):
        xsta = 1027
    elif (valueAcftType == "737-700") and (valueStafwd == "867"):
        xsta = 1047
    elif (valueAcftType == "737-700") and (valueStafwd == "887"):
        xsta = 1067
    elif (valueAcftType == "737-700") and (valueStafwd == "907"):
        xsta = 1087
    elif (valueAcftType == "737-700") and (valueStafwd == "927"):
        xsta = 1107
    elif (valueAcftType == "737-700") and (valueStafwd == "947.5"):
        xsta = 1127.5
    elif (valueAcftType == "737-700") and (valueStafwd == "951"):
        xsta = 1131
    elif (valueAcftType == "737-700") and (valueStafwd == "967"):
        xsta = 1147
    elif (valueAcftType == "737-700") and (valueStafwd == "986.5"):
        xsta = 1166.5
    elif (valueAcftType == "737-700") and (valueStafwd == "992.8"):
        xsta = 1169.7
    elif (valueAcftType == "737-700") and (valueStafwd == "1006"):
        xsta = 1186
    elif (valueAcftType == "737-700") and (valueStafwd == "1016"):
        xsta = 1196
    elif (valueAcftType == "737-700") and (valueStafwd == "1040"):
        xsta = 1220
    elif (valueAcftType == "737-700") and (valueStafwd == "1064"):
        xsta = 1244
    elif (valueAcftType == "737-700") and (valueStafwd == "1088"):
        xsta = 1268
    elif (valueAcftType == "737-700") and (valueStafwd == "1104"):
        xsta = 1284
    elif (valueAcftType == "737-700") and (valueStafwd == "1112"):
        xsta = 1292
    elif (valueAcftType == "737-700") and (valueStafwd == "1121"):
        xsta = 1292
    elif (valueAcftType == "737-700") and (valueStafwd == "1129"):
        xsta = 1309
    elif (valueAcftType == "737-700") and (valueStafwd == "1138"):
        xsta = 1318
    elif (valueAcftType == "737-700") and (valueStafwd == "1156"):
        xsta = 1336
    elif (valueAcftType == "737-700") and (valueStafwd == "1217"):
        xsta = 1397


# 737-700 and Aft Sta Value
    if (valueAcftType == "737-700") and (valueStaaft == "130"):
        ysta = 130
    elif (valueAcftType == "737-700") and (valueStaaft == "178"):
        ysta = 178
    elif (valueAcftType == "737-700") and (valueStaaft == "259.5"):
        ysta = 259.9
    elif (valueAcftType == "737-700") and (valueStaaft == "360"):
        ysta = 360
    elif (valueAcftType == "737-700") and (valueStaaft == "380"):
        ysta = 380
    elif (valueAcftType == "737-700") and (valueStaaft == "400"):
        ysta = 400
    elif (valueAcftType == "737-700") and (valueStaaft == "420"):
        ysta = 420
    elif (valueAcftType == "737-700") and (valueStaaft == "440"):
        ysta = 440
    elif (valueAcftType == "737-700") and (valueStaaft == "460"):
        ysta = 460
    elif (valueAcftType == "737-700") and (valueStaaft == "480"):
        ysta = 480
    elif (valueAcftType == "737-700") and (valueStaaft == "500"):
        ysta = 500
    elif (valueAcftType == "737-700") and (valueStaaft == "500A"):
        ysta = 520
    elif (valueAcftType == "737-700") and (valueStaaft == "500B"):
        ysta = 540
    elif (valueAcftType == "737-700") and (valueStaaft == "500C"):
        ysta = 560
    elif (valueAcftType == "737-700") and (valueStaaft == "500D"):
        ysta = 580
    elif (valueAcftType == "737-700") and (valueStaaft == "500E"):
        ysta = 0
    elif (valueAcftType == "737-700") and (valueStaaft == "500F"):
        ysta = 0
    elif (valueAcftType == "737-700") and (valueStaaft == "500G"):
        ysta = 0
    elif (valueAcftType == "737-700") and (valueStaaft == "500H"):
        ysta = 0
    elif (valueAcftType == "737-700") and (valueStaaft == "500I"):
        ysta = 0
    elif (valueAcftType == "737-700") and (valueStaaft == "500J"):
        ysta = 0
    elif (valueAcftType == "737-700") and (valueStaaft == "500K"):
        ysta = 0
    elif (valueAcftType == "737-700") and (valueStaaft == "500L"):
        ysta = 0
    elif (valueAcftType == "737-700") and (valueStaaft == "520"):
        ysta = 600
    elif (valueAcftType == "737-700") and (valueStaaft == "540"):
        ysta = 620
    elif (valueAcftType == "737-700") and (valueStaaft == "559"):
        ysta = 639
    elif (valueAcftType == "737-700") and (valueStaaft == "578"):
        ysta = 658
    elif (valueAcftType == "737-700") and (valueStaaft == "597"):
        ysta = 676
    elif (valueAcftType == "737-700") and (valueStaaft == "616"):
        ysta = 696
    elif (valueAcftType == "737-700") and (valueStaaft == "639"):
        ysta = 719
    elif (valueAcftType == "737-700") and (valueStaaft == "663.75"):
        ysta = 743.5
    elif (valueAcftType == "737-700") and (valueStaaft == "685"):
        ysta = 765
    elif (valueAcftType == "737-700") and (valueStaaft == "706"):
        ysta = 786
    elif (valueAcftType == "737-700") and (valueStaaft == "727"):
        ysta = 807
    elif (valueAcftType == "737-700") and (valueStaaft == "727A"):
        ysta = 827
    elif (valueAcftType == "737-700") and (valueStaaft == "727B"):
        ysta = 847
    elif (valueAcftType == "737-700") and (valueStaaft == "727C"):
        ysta = 867
    elif (valueAcftType == "737-700") and (valueStaaft == "727D"):
        ysta = 887
    elif (valueAcftType == "737-700") and (valueStaaft == "727E"):
        ysta = 0
    elif (valueAcftType == "737-700") and (valueStaaft == "727F"):
        ysta = 0
    elif (valueAcftType == "737-700") and (valueStaaft == "727G"):
        ysta = 0
    elif (valueAcftType == "737-700") and (valueStaaft == "727H"):
        ysta = 0
    elif (valueAcftType == "737-700") and (valueStaaft == "727G"):
        ysta = 0
    elif (valueAcftType == "737-700") and (valueStaaft == "727H"):
        ysta = 0
    elif (valueAcftType == "737-700") and (valueStaaft == "727I"):
        ysta = 0
    elif (valueAcftType == "737-700") and (valueStaaft == "727J"):
        ysta = 0
    elif (valueAcftType == "737-700") and (valueStaaft == "727K"):
        ysta = 0
    elif (valueAcftType == "737-700") and (valueStaaft == "727J"):
        ysta = 0
    elif (valueAcftType == "737-700") and (valueStaaft == "727L"):
        ysta = 0
    elif (valueAcftType == "737-700") and (valueStaaft == "747"):
        ysta = 927
    elif (valueAcftType == "737-700") and (valueStaaft == "767"):
        ysta = 947
    elif (valueAcftType == "737-700") and (valueStaaft == "787"):
        ysta = 967
    elif (valueAcftType == "737-700") and (valueStaaft == "807"):
        ysta = 987
    elif (valueAcftType == "737-700") and (valueStaaft == "827"):
        ysta = 1007
    elif (valueAcftType == "737-700") and (valueStaaft == "847"):
        ysta = 1027
    elif (valueAcftType == "737-700") and (valueStaaft == "867"):
        ysta = 1047
    elif (valueAcftType == "737-700") and (valueStaaft == "887"):
        ysta = 1067
    elif (valueAcftType == "737-700") and (valueStaaft == "907"):
        ysta = 1087
    elif (valueAcftType == "737-700") and (valueStaaft == "927"):
        ysta = 1107
    elif (valueAcftType == "737-700") and (valueStaaft == "947.5"):
        ysta = 1127.5
    elif (valueAcftType == "737-700") and (valueStaaft == "951"):
        ysta = 1131
    elif (valueAcftType == "737-700") and (valueStaaft == "967"):
        ysta = 1147
    elif (valueAcftType == "737-700") and (valueStaaft == "986.5"):
        ysta = 1166.5
    elif (valueAcftType == "737-700") and (valueStaaft == "992.8"):
        ysta = 1169.7
    elif (valueAcftType == "737-700") and (valueStaaft == "1006"):
        ysta = 1186
    elif (valueAcftType == "737-700") and (valueStaaft == "1016"):
        ysta = 1196
    elif (valueAcftType == "737-700") and (valueStaaft == "1040"):
        ysta = 1220
    elif (valueAcftType == "737-700") and (valueStaaft == "1064"):
        ysta = 1244
    elif (valueAcftType == "737-700") and (valueStaaft == "1088"):
        ysta = 1268
    elif (valueAcftType == "737-700") and (valueStaaft == "1104"):
        ysta = 1284
    elif (valueAcftType == "737-700") and (valueStaaft == "1112"):
        ysta = 1292
    elif (valueAcftType == "737-700") and (valueStaaft == "1121"):
        ysta = 1292
    elif (valueAcftType == "737-700") and (valueStaaft == "1129"):
        ysta = 1309
    elif (valueAcftType == "737-700") and (valueStaaft == "1138"):
        ysta = 1318
    elif (valueAcftType == "737-700") and (valueStaaft == "1156"):
        ysta = 1336
    elif (valueAcftType == "737-700") and (valueStaaft == "1217"):
        ysta = 1397


# 737-800 and FWD Sta Value
    if (valueAcftType == "737-800") and (valueStafwd == "130"):
        xsta = 130
    elif (valueAcftType == "737-800") and (valueStafwd == "178"):
        xsta = 178
    elif (valueAcftType == "737-800") and (valueStafwd == "259.5"):
        xsta = 259.9
    elif (valueAcftType == "737-800") and (valueStafwd == "360"):
        xsta = 360
    elif (valueAcftType == "737-800") and (valueStafwd == "380"):
        xsta = 380
    elif (valueAcftType == "737-800") and (valueStafwd == "400"):
        xsta = 400
    elif (valueAcftType == "737-800") and (valueStafwd == "420"):
        xsta = 420
    elif (valueAcftType == "737-800") and (valueStafwd == "440"):
        xsta = 440
    elif (valueAcftType == "737-800") and (valueStafwd == "460"):
        xsta = 460
    elif (valueAcftType == "737-800") and (valueStafwd == "480"):
        xsta = 480
    elif (valueAcftType == "737-800") and (valueStafwd == "500"):
        xsta = 500
    elif (valueAcftType == "737-800") and (valueStafwd == "500A"):
        xsta = 522
    elif (valueAcftType == "737-800") and (valueStafwd == "500B"):
        xsta = 544
    elif (valueAcftType == "737-800") and (valueStafwd == "500C"):
        xsta = 566
    elif (valueAcftType == "737-800") and (valueStafwd == "500D"):
        xsta = 588
    elif (valueAcftType == "737-800") and (valueStafwd == "500E"):
        xsta = 610
    elif (valueAcftType == "737-800") and (valueStafwd == "500F"):
        xsta = 632
    elif (valueAcftType == "737-800") and (valueStafwd == "500G"):
        xsta = 654
    elif (valueAcftType == "737-800") and (valueStafwd == "500H"):
        xsta = 676
    elif (valueAcftType == "737-800") and (valueStafwd == "500I"):
        xsta = 698
    elif (valueAcftType == "737-800") and (valueStafwd == "500J"):
        xsta = 0
    elif (valueAcftType == "737-800") and (valueStafwd == "500K"):
        xsta = 0
    elif (valueAcftType == "737-800") and (valueStafwd == "500L"):
        xsta = 0
    elif (valueAcftType == "737-800") and (valueStafwd == "520"):
        xsta = 718
    elif (valueAcftType == "737-800") and (valueStafwd == "540"):
        xsta = 738
    elif (valueAcftType == "737-800") and (valueStafwd == "559"):
        xsta = 757
    elif (valueAcftType == "737-800") and (valueStafwd == "578"):
        xsta = 776
    elif (valueAcftType == "737-800") and (valueStafwd == "597"):
        xsta = 794
    elif (valueAcftType == "737-800") and (valueStafwd == "616"):
        xsta = 814
    elif (valueAcftType == "737-800") and (valueStafwd == "639"):
        xsta = 837
    elif (valueAcftType == "737-800") and (valueStafwd == "663.75"):
        xsta = 861.75
    elif (valueAcftType == "737-800") and (valueStafwd == "685"):
        xsta = 883
    elif (valueAcftType == "737-800") and (valueStafwd == "706"):
        xsta = 904
    elif (valueAcftType == "737-800") and (valueStafwd == "727"):
        xsta = 925
    elif (valueAcftType == "737-800") and (valueStafwd == "727A"):
        xsta = 945
    elif (valueAcftType == "737-800") and (valueStafwd == "727B"):
        xsta = 965
    elif (valueAcftType == "737-800") and (valueStafwd == "727C"):
        xsta = 985
    elif (valueAcftType == "737-800") and (valueStafwd == "727D"):
        xsta = 1007
    elif (valueAcftType == "737-800") and (valueStafwd == "727E"):
        xsta = 1029
    elif (valueAcftType == "737-800") and (valueStafwd == "727F"):
        xsta = 1051
    elif (valueAcftType == "737-800") and (valueStafwd == "727G"):
        xsta = 1073
    elif (valueAcftType == "737-800") and (valueStafwd == "727H"):
        xsta = 1095
    elif (valueAcftType == "737-800") and (valueStafwd == "727I"):
        xsta = 1137
    elif (valueAcftType == "737-800") and (valueStafwd == "727J"):
        xsta = 0
    elif (valueAcftType == "737-800") and (valueStafwd == "727K"):
        xsta = 0
    elif (valueAcftType == "737-800") and (valueStafwd == "747"):
        xsta = 1157
    elif (valueAcftType == "737-800") and (valueStafwd == "767"):
        xsta = 1177
    elif (valueAcftType == "737-800") and (valueStafwd == "787"):
        xsta = 1197
    elif (valueAcftType == "737-800") and (valueStafwd == "807"):
        xsta = 1217
    elif (valueAcftType == "737-800") and (valueStafwd == "827"):
        xsta = 1237
    elif (valueAcftType == "737-800") and (valueStafwd == "847"):
        xsta = 1257
    elif (valueAcftType == "737-800") and (valueStafwd == "867"):
        xsta = 1277
    elif (valueAcftType == "737-800") and (valueStafwd == "887"):
        xsta = 1297
    elif (valueAcftType == "737-800") and (valueStafwd == "907"):
        xsta = 1317
    elif (valueAcftType == "737-800") and (valueStafwd == "927"):
        xsta = 1337
    elif (valueAcftType == "737-800") and (valueStafwd == "947.5"):
        xsta = 1357.5
    elif (valueAcftType == "737-800") and (valueStafwd == "951"):
        xsta = 1361
    elif (valueAcftType == "737-800") and (valueStafwd == "967"):
        xsta = 1377
    elif (valueAcftType == "737-800") and (valueStafwd == "986.5"):
        xsta = 1396.5
    elif (valueAcftType == "737-800") and (valueStafwd == "992.8"):
        xsta = 1402.8
    elif (valueAcftType == "737-800") and (valueStafwd == "1006"):
        xsta = 1416
    elif (valueAcftType == "737-800") and (valueStafwd == "1016"):
        xsta = 1426
    elif (valueAcftType == "737-800") and (valueStafwd == "1040"):
        xsta = 1450
    elif (valueAcftType == "737-800") and (valueStafwd == "1064"):
        xsta = 1474
    elif (valueAcftType == "737-800") and (valueStafwd == "1088"):
        xsta = 1498
    elif (valueAcftType == "737-800") and (valueStafwd == "1104"):
        xsta = 1514
    elif (valueAcftType == "737-800") and (valueStafwd == "1112"):
        xsta = 1522
    elif (valueAcftType == "737-800") and (valueStafwd == "1121"):
        xsta = 1531
    elif (valueAcftType == "737-800") and (valueStafwd == "1129"):
        xsta = 1539
    elif (valueAcftType == "737-800") and (valueStafwd == "1138"):
        xsta = 1548
    elif (valueAcftType == "737-800") and (valueStafwd == "1156"):
        xsta = 1566
    elif (valueAcftType == "737-800") and (valueStafwd == "1217"):
        xsta = 1627


# 737-800 and AFT Sta Value
    if (valueAcftType == "737-800") and (valueStaaft == "130"):
        ysta = 130
    elif (valueAcftType == "737-800") and (valueStaaft == "178"):
        ysta = 178
    elif (valueAcftType == "737-800") and (valueStaaft == "259.5"):
        ysta = 259.9
    elif (valueAcftType == "737-800") and (valueStaaft == "360"):
        ysta = 360
    elif (valueAcftType == "737-800") and (valueStaaft == "380"):
        ysta = 380
    elif (valueAcftType == "737-800") and (valueStaaft == "400"):
        ysta = 400
    elif (valueAcftType == "737-800") and (valueStaaft == "420"):
        ysta = 420
    elif (valueAcftType == "737-800") and (valueStaaft == "440"):
        ysta = 440
    elif (valueAcftType == "737-800") and (valueStaaft == "460"):
        ysta = 460
    elif (valueAcftType == "737-800") and (valueStaaft == "480"):
        ysta = 480
    elif (valueAcftType == "737-800") and (valueStaaft == "500"):
        ysta = 500
    elif (valueAcftType == "737-800") and (valueStaaft == "500A"):
        ysta = 522
    elif (valueAcftType == "737-800") and (valueStaaft == "500B"):
        ysta = 544
    elif (valueAcftType == "737-800") and (valueStaaft == "500C"):
        ysta = 566
    elif (valueAcftType == "737-800") and (valueStaaft == "500D"):
        ysta = 588
    elif (valueAcftType == "737-800") and (valueStaaft == "500E"):
        ysta = 610
    elif (valueAcftType == "737-800") and (valueStaaft == "500F"):
        ysta = 632
    elif (valueAcftType == "737-800") and (valueStaaft == "500G"):
        ysta = 654
    elif (valueAcftType == "737-800") and (valueStaaft == "500H"):
        ysta = 676
    elif (valueAcftType == "737-800") and (valueStaaft == "500I"):
        ysta = 698
    elif (valueAcftType == "737-800") and (valueStaaft == "500J"):
        ysta = 0
    elif (valueAcftType == "737-800") and (valueStaaft == "500K"):
        ysta = 0
    elif (valueAcftType == "737-800") and (valueStaaft == "500L"):
        ysta = 0
    elif (valueAcftType == "737-800") and (valueStaaft == "520"):
        ysta = 718
    elif (valueAcftType == "737-800") and (valueStaaft == "540"):
        ysta = 738
    elif (valueAcftType == "737-800") and (valueStaaft == "559"):
        ysta = 757
    elif (valueAcftType == "737-800") and (valueStaaft == "578"):
        ysta = 776
    elif (valueAcftType == "737-800") and (valueStaaft == "597"):
        ysta = 794
    elif (valueAcftType == "737-800") and (valueStaaft == "616"):
        ysta = 814
    elif (valueAcftType == "737-800") and (valueStaaft == "639"):
        ysta = 837
    elif (valueAcftType == "737-800") and (valueStaaft == "663.75"):
        ysta = 861.75
    elif (valueAcftType == "737-800") and (valueStaaft == "685"):
        ysta = 883
    elif (valueAcftType == "737-800") and (valueStaaft == "706"):
        ysta = 904
    elif (valueAcftType == "737-800") and (valueStaaft == "727"):
        ysta = 925
    elif (valueAcftType == "737-800") and (valueStaaft == "727A"):
        ysta = 945
    elif (valueAcftType == "737-800") and (valueStaaft == "727B"):
        ysta = 965
    elif (valueAcftType == "737-800") and (valueStaaft == "727C"):
        ysta = 985
    elif (valueAcftType == "737-800") and (valueStaaft == "727D"):
        ysta = 1007
    elif (valueAcftType == "737-800") and (valueStaaft == "727E"):
        ysta = 1029
    elif (valueAcftType == "737-800") and (valueStaaft == "727F"):
        ysta = 1051
    elif (valueAcftType == "737-800") and (valueStaaft == "727G"):
        ysta = 1073
    elif (valueAcftType == "737-800") and (valueStaaft == "727H"):
        ysta = 1095
    elif (valueAcftType == "737-800") and (valueStaaft == "727I"):
        ysta = 1137
    elif (valueAcftType == "737-800") and (valueStaaft == "727J"):
        ysta = 0
    elif (valueAcftType == "737-800") and (valueStaaft == "727K"):
        ysta = 0
    elif (valueAcftType == "737-800") and (valueStaaft == "747"):
        ysta = 1157
    elif (valueAcftType == "737-800") and (valueStaaft == "767"):
        ysta = 1177
    elif (valueAcftType == "737-800") and (valueStaaft == "787"):
        ysta = 1197
    elif (valueAcftType == "737-800") and (valueStaaft == "807"):
        ysta = 1217
    elif (valueAcftType == "737-800") and (valueStaaft == "827"):
        ysta = 1237
    elif (valueAcftType == "737-800") and (valueStaaft == "847"):
        ysta = 1257
    elif (valueAcftType == "737-800") and (valueStaaft == "867"):
        ysta = 1277
    elif (valueAcftType == "737-800") and (valueStaaft == "887"):
        ysta = 1297
    elif (valueAcftType == "737-800") and (valueStaaft == "907"):
        ysta = 1317
    elif (valueAcftType == "737-800") and (valueStaaft == "927"):
        ysta = 1337
    elif (valueAcftType == "737-800") and (valueStaaft == "947.5"):
        ysta = 1357.5
    elif (valueAcftType == "737-800") and (valueStaaft == "951"):
        ysta = 1361
    elif (valueAcftType == "737-800") and (valueStaaft == "967"):
        ysta = 1377
    elif (valueAcftType == "737-800") and (valueStaaft == "986.5"):
        ysta = 1396.5
    elif (valueAcftType == "737-800") and (valueStaaft == "992.8"):
        ysta = 1402.8
    elif (valueAcftType == "737-800") and (valueStaaft == "1006"):
        ysta = 1416
    elif (valueAcftType == "737-800") and (valueStaaft == "1016"):
        ysta = 1426
    elif (valueAcftType == "737-800") and (valueStaaft == "1040"):
        ysta = 1450
    elif (valueAcftType == "737-800") and (valueStaaft == "1064"):
        ysta = 1474
    elif (valueAcftType == "737-800") and (valueStaaft == "1088"):
        ysta = 1498
    elif (valueAcftType == "737-800") and (valueStaaft == "1104"):
        ysta = 1514
    elif (valueAcftType == "737-800") and (valueStaaft == "1112"):
        ysta = 1522
    elif (valueAcftType == "737-800") and (valueStaaft == "1121"):
        ysta = 1531
    elif (valueAcftType == "737-800") and (valueStaaft == "1129"):
        ysta = 1539
    elif (valueAcftType == "737-800") and (valueStaaft == "1138"):
        ysta = 1548
    elif (valueAcftType == "737-800") and (valueStaaft == "1156"):
        ysta = 1566
    elif (valueAcftType == "737-800") and (valueStaaft == "1217"):
        ysta = 1627

# FWD STR Value
    if valueStrStart == "1":
        xstr = 306.5
        xbl = 0
        fangle = 0
    elif valueStrStart == "2":
        xstr = 306.5
        xbl = 9.6
        fangle = 5.625
    elif valueStrStart == "3":
        xstr = 304
        xbl = 19
        fangle = 11.25
    elif valueStrStart == "4":
        xstr = 301
        xbl = 28.1
        fangle = 16.875
    elif valueStrStart == "5":
        xstr = 296.8
        xbl = 36.7
        fangle = 22.5
    elif valueStrStart == "6":
        xstr = 291.5
        xbl = 44.7
        fangle = 28.125
    elif valueStrStart == "7":
        xstr = 285.2
        xbl = 52.0
        fangle = 33.75
    elif valueStrStart == "8":
        xstr = 278.4
        xbl = 58.1
        fangle = 39.375
    elif valueStrStart == "9":
        xstr = 270.8
        xbl = 63.3
        fangle = 45
    elif valueStrStart == "10":
        xstr = 262.7
        xbl = 67.6
        fangle = 50.625
    elif valueStrStart == "11":
        xstr = 245.1
        xbl = 70.8
        fangle = 56.25
    elif valueStrStart == "12":
        xstr = 246.1
        xbl = 72.2
        fangle = 61.875
    elif valueStrStart == "13":
        xstr = 238.0
        xbl = 73.8
        fangle = 67.5
    elif valueStrStart == "14":
        xstr = 230.3
        xbl = 74.0
        fangle = 73.125
    elif valueStrStart == "15":
        xstr = 222.8
        xbl = 73.4
        fangle = 78.75
    elif valueStrStart == "16":
        xstr = 215.3
        xbl = 72.1
        fangle = 84.375
    elif valueStrStart == "17":
        xstr = 188.8
        xbl = 68.6
        fangle = 90
    elif valueStrStart == "18":
        xstr = 198.2
        xbl = 68.4
    elif valueStrStart == "19":
        xstr = 190.3
        xbl = 65.5
    elif valueStrStart == "20":
        xstr = 182.9
        xbl = 61.7
    elif valueStrStart == "21":
        xstr = 175.9
        xbl = 57.0
    elif valueStrStart == "22":
        xstr = 169.6
        xbl = 51.5
    elif valueStrStart == "23":
        xstr = 164.1
        xbl = 45.3
    elif valueStrStart == "24":
        xstr = 159.2
        xbl = 38.5
    elif valueStrStart == "25":
        xstr = 155.3
        xbl = 31.1
    elif valueStrStart == "26":
        xstr = 152.2
        xbl = 23.3
    elif valueStrStart == "28":
        xstr = 148.8
        xbl = 6.5

# AFT STR Value
    if valueStrEnd == "1":
        ystr = 306.5
        ybl = 0
        aangle = 0
    elif valueStrEnd == "2":
        ystr = 306.5
        ybl = 9.6
        aangle = 5.625
    elif valueStrEnd == "3":
        ystr = 304
        ybl = 19
        aangle = 11.25
    elif valueStrEnd == "4":
        ystr = 301
        ybl = 28.1
        aangle = 16.875
    elif valueStrEnd == "5":
        ystr = 296.8
        ybl = 36.7
        aangle = 22.5
    elif valueStrEnd == "6":
        ystr = 291.5
        ybl = 44.7
        aangle = 28.125
    elif valueStrEnd == "7":
        ystr = 285.2
        ybl = 52.0
        aangle = 33.75
    elif valueStrEnd == "8":
        ystr = 278.4
        ybl = 58.1
        aangle = 39.375
    elif valueStrEnd == "9":
        ystr = 270.8
        ybl = 63.3
        aangle = 45
    elif valueStrEnd == "10":
        ystr = 262.7
        ybl = 67.6
        aangle = 50.625
    elif valueStrEnd == "11":
        ystr = 245.1
        ybl = 70.8
        aangle = 56.25
    elif valueStrEnd == "12":
        ystr = 246.1
        ybl = 72.2
        aangle = 61.875
    elif valueStrEnd == "13":
        ystr = 238.0
        ybl = 73.8
        aangle = 67.5
    elif valueStrEnd == "14":
        ystr = 230.3
        ybl = 74.0
        aangle = 73.125
    elif valueStrEnd == "15":
        ystr = 222.8
        ybl = 73.4
        aangle = 78.75
    elif valueStrEnd == "16":
        ystr = 215.3
        ybl = 72.1
        aangle = 84.375
    elif valueStrEnd == "17":
        ystr = 188.8
        ybl = 68.6
        aangle = 90
    elif valueStrEnd == "18":
        ystr = 198.2
        ybl = 68.4
    elif valueStrEnd == "19":
        ystr = 190.3
        ybl = 65.5
    elif valueStrEnd == "20":
        ystr = 182.9
        ybl = 61.7
    elif valueStrEnd == "21":
        ystr = 175.9
        ybl = 57.0
    elif valueStrEnd == "22":
        ystr = 169.6
        ybl = 51.5
    elif valueStrEnd == "23":
        ystr = 164.1
        ybl = 45.3
    elif valueStrEnd == "24":
        ystr = 159.2
        ybl = 38.5
    elif valueStrEnd == "25":
        ystr = 155.3
        ybl = 31.1
    elif valueStrEnd == "26":
        ystr = 152.2
        ybl = 23.3
    elif valueStrEnd == "28":
        ystr = 148.8
        ybl = 6.59

    print("X Sta= ", xsta)
    print("y Sta= ", ysta)
    print("x Str= ", xstr)
    print("y Str= ", ystr)
    print("x BL= ", xbl)
    print("y BL= ", ybl)
    print("cross= ", crossVar)

#Set Station
    if xsta > ysta:
        zsta = xsta - ysta
    elif ysta > xsta:
        zsta = ysta - xsta
    elif xsta == ysta:
        zsta = 0

#Set Bl Side (Left or Right) if Moving from Side to Side add value.
    if (valueBlStart == 0) and (valueBlEnd == 0):
        zvalueBl = 0
    elif (valueBlStart == 1) and (valueBlEnd == 0):
        zvalueBl = 72
    elif (valueBlStart == 0) and (valueBlEnd == 1):
        zvalueBl = 72
    elif (valueBlStart == 1) and (valueBlEnd == 1):
        zvalueBl = 0

    xbl = ((2*(math.pi))*74)*(fangle/360)
    ybl = ((2*(math.pi))*74)*(aangle/360)

    # Set Station
    if xbl > ybl:
        zbl = xbl - ybl
        xbl = 0
        ybl = 0
    elif ybl > xbl:
        zbl = ybl - xbl
        xbl = 0
        ybl = 0
    elif xbl == ybl:
        zbl = 0
        xbl = 0
        ybl = 0
    elif (xbl == ybl) and (valueBlStart == valueBlEnd):
        ybl = ybl
        xbl = xbl
        zbl = 0

    total = (zsta + zvalueBl + xbl + ybl + zbl + crossVar) / (1-(valueOverage/100))
    print("Total: ", total)
    total = round(total, 0)
    totallabel["text"]= total

'''
    if xstr > ystr:
        zstr = (xstr - ystr) * 1.20
    elif ystr > xstr:
        zstr = (ystr - xstr) * 1.20
    else: zstr = 0
'''


root = ttkb.Window(themename="superhero")
# root = Tk()


root.title("Wire Calculator")
root.geometry('740x700')
cross = IntVar()
BlStart = IntVar()
BlEnd = IntVar()

my_label = ttkb.Label(text="Wire Calculator", font=("Helvetica", 16), bootstyle="light")
my_label.grid(row=0, column=2, pady=10)

my_label = ttkb.Label(text="Aircraft Type", font=("Helvetica", 10), bootstyle="light")
my_label.grid(row=1, column=0, padx=5, pady=5)

# Aircraft Type Combobox

acfttype = ttkb.StringVar()
acfttypeDp = ttkb.Combobox(width=10, textvariable=acfttype, state='readonly')
acfttypeDp.grid(row=1, column=1, pady=10)
acfttypeDp['values'] = ('737-700', '737-800')

acfttypeDp.current(1)
acfttypeDp.bind("<<ComboboxSelected>>", selection_acfttype)

my_label = ttkb.Label(text="Station Start", font=("Helvetica", 10), bootstyle="light")
my_label.grid(row=2, column=0, pady=5)

# Station Start Combobox

nfwd = ttkb.StringVar()
stafwd = ttkb.Combobox(width=10, textvariable=nfwd, state='readonly', justify='center')
stafwd.grid(row=2, column=1, pady=5, padx=5)
stafwd['values'] = ('130', '178', '259.5', '360', '380', '400', '420', '440', '460', '480', '500',
                    '500A', '500B', '500C', '500D', '500E', '500F', '500G', '500H', '500I', '500J', '500K', '500L',
                    '520', '540', '559', '578', '597', '616', '639', '663.75', '685', '706', '727',
                    '727A', '727B', '727C', '727D', '727E', '727F', '727G', '727H', '727I', '727J', '727K', '727L',
                    '747', '767', '787', '807', '827', '847', '867', '887',
                    '907', '927', '947.5', '951', '967', '986.5', '992.8', '1006', '1016',
                    '1040', '1064', '1088', '1104', '1112', '1121', '1129', '1138', '1156', '1217')
stafwd.current(1)
stafwd.bind("<<ComboboxSelected>>", selection_changedfwd)

my_label = ttkb.Label(text="Station End", font=("Helvetica", 10), bootstyle="light")
my_label.grid(row=3, column=0, padx=5, pady=5)

# Station End Combobox

naft = ttkb.StringVar()
staaft = ttkb.Combobox(width=10, textvariable=naft, state="readonly", justify='center')
staaft.grid(row=3, column=1, padx=5, pady=10)
staaft['values'] = ('130', '178', '259.5', '360', '380', '400', '420', '440', '460', '480', '500',
                    '500A', '500B', '500C', '500D', '500E', '500F', '500G', '500H', '500I', '500J', '500K', '500L',
                    '520', '540', '559', '578', '597', '616', '639', '663.75', '685', '706', '727',
                    '727A', '727B', '727C', '727D', '727E', '727F', '727G', '727H', '727I', '727J', '727K', '727L',
                    '747', '767', '787', '807', '827', '847', '867', '887',
                    '907', '927', '947.5', '951', '967', '986.5', '992.8', '1006', '1016',
                    '1040', '1064', '1088', '1104', '1112', '1121', '1129', '1138', '1156', '1217')
staaft.current(1)
staaft.bind("<<ComboboxSelected>>", selection_changedaft)

# Str Start Combobox

strStart = ttkb.StringVar()
strStart = ttkb.Combobox(width=10, textvariable=strStart, state="readonly", justify='center')
strStart.grid(row=2, column=2, padx=5, pady=10)
strStart['values'] = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16',
                      '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28')
strStart.current(1)
strStart.bind("<<ComboboxSelected>>", selection_strStart)

strStartLabel = ttkb.Label(root, text="Left Side")
strStartLabel.grid(row=2, column=3)

# Str Start RH or LH
strStartCheckBox = ttkb.Checkbutton(root, text="Right Side", state="selected", style="roundToggle", offvalue=0, onvalue=1, variable=BlStart)
strStartCheckBox.grid(row=2, column=4)

# Str End Combobox
strEnd = ttkb.StringVar()
strEnd = ttkb.Combobox(width=10, textvariable=strEnd, state="readonly", justify='center')
strEnd.grid(row=3, column=2, padx=5, pady=10)
strEnd['values'] = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16',
                    '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28')
strEnd.current(1)
strEnd.bind("<<ComboboxSelected>>", selection_strEnd)

strEndLabel = ttkb.Label(root, text="Left Side")
strEndLabel.grid(row=3, column=3)

# Str Start RH or LH
strEndCheckBox = ttkb.Checkbutton(root, text="Right Side", style="roundToggle", offvalue=0, onvalue=1, variable=BlEnd)
strEndCheckBox.grid(row=3, column=4)


#Crossover Checkbox
crossCheckBox = ttkb.Checkbutton(root, text="Include Crossover?", style="roundToggle", offvalue=1, onvalue=72, variable=cross)
crossCheckBox.grid(row=12, column=2, pady= 10)

overPercentLabel = ttkb.Label(root, text="Overage %")
overPercentLabel.grid(row=14, column=1)

overPercent = ttkb.Entry(justify='center', style="info", width=5)
overPercent = ttkb.Entry(root, textvariable=int)
overPercent.insert(0, 15)

overPercent.grid(row=14, column=2, pady=20)

#submit button
submitButton = ttkb.Button(bootstyle="success", text="Calculate", command=submitButton)
submitButton.grid(row=15, column=2)

#total label
totallabel = ttkb.Label(root, text="Total(in)", justify= 'left')
totallabel.grid(row=17, column=2, pady= 20)


root.mainloop()
