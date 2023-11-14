# -*- coding: utf-8 -*-

import empro.toolkit.adv as adv

def main():
	path=r"C:/Users/m-hug/Documents/GitHub/SAELoRaWAN/ADS/SAELoRaWAN_wrk"
	lib=r"SAELoRaWAN_lib"
	subst=r"SAELoRaWAN_lib/substrateLORA.subst"
	substlib=r"SAELoRaWAN_lib"
	substname=r"substrateLORA"
	cell=r"antenneLORA"
	view=r"layout"
	libS3D=r"simulation/SAELoRaWAN_lib/antenne%L%O%R%A/_3%D%Viewer/extra/0/proj_libS3D.xml"
	varDictionary={}
	exprDictionary={}
	adv.loadDesign(path=path, lib=lib, subst=subst, substlib=substlib, substname=substname, cell=cell, view=view, libS3D=libS3D, var_dict=varDictionary, expr_dict=exprDictionary)
