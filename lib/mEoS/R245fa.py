#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''Pychemqt, Chemical Engineering Process simulator
Copyright (C) 2016, Juan José Gómez Romera <jjgomera@gmail.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.'''


from lib.meos import MEoS
from lib import unidades


class R245fa(MEoS):
    """Multiparameter equation of state for R245fa"""
    name = "1,1,1,3,3-pentafluoropropane"
    CASNumber = "460-73-1"
    formula = "CF3CH2CHF2"
    synonym = "R245fa"
    rhoc = unidades.Density(519.43577)
    Tc = unidades.Temperature(427.01)
    Pc = unidades.Pressure(3651.0, "kPa")
    M = 134.04794  # g/mol
    Tt = unidades.Temperature(170.0)
    Tb = unidades.Temperature(288.198)
    f_acent = 0.3783
    momentoDipolar = unidades.DipoleMoment(1.549, "Debye")
    id = 671
    # id = 1817

    Fi1 = {"ao_log": [1, 3.],
           "pow": [0, 1],
           "ao_pow": [-13.38560883, 9.845374371],
           "ao_exp": [5.5728, 10.385, 12.554],
           "titao": [222/Tc, 1010/Tc, 2450/Tc]}

    Fi2 = {"ao_log": [1, 3.],
           "pow": [0, 1],
           "ao_pow": [-13.4283638514, 9.87236538],
           "ao_exp": [5.5728, 10.385, 12.554],
           "titao": [222/Tc, 1010/Tc, 2450/Tc]}

    helmholtz1 = {
        "__type__": "Helmholtz",
        "__name__": "Helmholtz equation of state for R-245fa of Akasaka (2015).",
        "__doi__": {"autor": "Akasaka, Ryo; Zhou, Yong; Lemmon, Eric W.",
                    "title": "Fundamental Equation of State for 1,1,1,3,3-Pentafluoropropane (R-245fa)",
                    "ref": "Journal of Physical and Chemical Reference Data 44, 013104 (2015)",
                    "doi":  "10.1063/1.4913493"},
        "__test__": """
            >>> st=R245fa(T=250, x=0.5)
            >>> print("%0.6g %0.7g %0.7g %0.7g %0.6g %0.6g %0.6g %0.6g %0.6g %0.6g %0.6g %0.6g %0.6g %0.6g" % (\
                st.T, st.P.MPa, st.Liquido.rhoM, st.Gas.rhoM, st.Liquido.hM.kJmol, st.Gas.hM.kJmol, \
                st.Liquido.sM.kJmolK, st.Gas.sM.kJmolK, st.Liquido.cvM.kJmolK, st.Gas.cvM.kJmolK, \
                st.Liquido.cpM.kJmolK, st.Gas.cpM.kJmolK, st.Liquido.w, st.Gas.w))
            250 0.01646009 10.90057 0.008011195 22.9621 51.9442 0.119346 0.235275 0.114156 0.0950838 0.163322 0.103970 873.234 128.702
            >>> st=R245fa(T=400, x=0.5)
            >>> print("%0.6g %0.7g %0.7g %0.7g %0.6g %0.6g %0.6g %0.6g %0.6g %0.6g %0.6g %0.6g %0.6g %0.6g" % (\
                st.T, st.P.MPa, st.Liquido.rhoM, st.Gas.rhoM, st.Liquido.hM.kJmol, st.Gas.hM.kJmol, \
                st.Liquido.sM.kJmolK, st.Gas.sM.kJmolK, st.Liquido.cvM.kJmolK, st.Gas.cvM.kJmolK, \
                st.Liquido.cpM.kJmolK, st.Gas.cpM.kJmolK, st.Liquido.w, st.Gas.w))
            400 2.210563 7.151900 1.068455 51.5591 65.2749 0.206989 0.241278 0.147755 0.148819 0.255135 0.234947 235.471 106.449
            >>> st=R245fa(T=250, rhom=11)
            >>> print("%0.6g %0.7g %0.7g %0.6g %0.6g %0.6g %0.6g %0.6g" % (\
                st.T, st.rhoM, st.P.MPa, st.hM.kJmol, st.sM.kJmolK, \
                st.cvM.kJmolK, st.cpM.kJmolK, st.w))
            250 11 7.454017 23.3683 0.118254 0.114536 0.162060 908.590
            >>> st=R245fa(T=250, rhom=0.005)
            >>> print("%0.6g %0.7g %0.7g %0.6g %0.6g %0.6g %0.6g %0.6g" % (\
                st.T, st.rhoM, st.P.MPa, st.hM.kJmol, st.sM.kJmolK, \
                st.cvM.kJmolK, st.cpM.kJmolK, st.w))
            250 0.005 0.01031829 51.9792 0.239262 0.0949026 0.103569 129.147
            >>> st=R245fa(T=400, rhom=9)
            >>> print("%0.6g %0.7g %0.7g %0.6g %0.6g %0.6g %0.6g %0.6g" % (\
                st.T, st.rhoM, st.P.MPa, st.hM.kJmol, st.sM.kJmolK, \
                st.cvM.kJmolK, st.cpM.kJmolK, st.w))
            400 9 33.14725 50.9308 0.196139 0.144117 0.188486 593.178
            >>> st=R245fa(T=400, rhom=0.5)
            >>> print("%0.6g %0.7g %0.7g %0.6g %0.6g %0.6g %0.6g %0.6g" % (\
                st.T, st.rhoM, st.P.MPa, st.hM.kJmol, st.sM.kJmolK, \
                st.cvM.kJmolK, st.cpM.kJmolK, st.w))
            400 0.5 1.352988 67.9067 0.250859 0.138842 0.162544 135.712
            """,  # Table 7, Pag 12

        "R": 8.314462,
        "cp": Fi1,
        "ref": {"Tref": 273.15, "Pref": 1., "ho": 54490.07, "so": 268.2193},

        "Tmin": Tt, "Tmax": 400.0, "Pmax": 200000.0, "rhomax": 12.3,
        "Pmin": 0.0125, "rhomin": 12.29,

        "nr1": [0.057506623, 1.5615975, -2.3614485, -0.51773521, 0.18509788],
        "d1": [4, 1, 1, 2, 3],
        "t1": [1, 0.27, 0.9, 1.09, 0.4],

        "nr2": [-.87405626, -.27530955, .57971151, -.39934306, -.033230277],
        "d2": [1, 3, 2, 2, 7],
        "t2": [2.9, 1.7, 0.8, 3.6, 1.05],
        "c2": [2, 2, 1, 2, 1],
        "gamma2": [1]*5,

        "nr3": [0.83210508, -0.33544300, -0.10117801, -0.0091495867],
        "d3": [1, 1, 3, 3],
        "t3": [1.8, 4.0, 4.5, 2.0],
        "alfa3": [1.011, 1.447, 1.079, 7.86],
        "beta3": [1.879, 2.454, 1.256, 21.1],
        "gamma3": [1.081, 0.651, 0.468, 1.293],
        "epsilon3": [0.709, 0.939, 0.703, 0.777]}

    helmholtz2 = {
        "__type__": "Helmholtz",
        "__name__": "short Helmholtz equation of state for R-245fa of Lemmon and Span (2006).",
        "__doi__": {"autor": "Lemmon, E.W., Span, R.",
                    "title": "Short Fundamental Equations of State for 20 Industrial Fluids",
                    "ref": "J. Chem. Eng. Data, 2006, 51 (3), pp 785–850",
                    "doi":  "10.1021/je050186n"},
        "__test__": """
            >>> st=R245fa(T=429, rho=3*134.04794, eq=1)
            >>> print("%0.0f %0.0f %0.3f %0.3f %0.3f %0.3f %0.3f %0.3f" % (st.T, st.rhoM, st.P.kPa, st.hM.kJkmol, st.sM.kJkmolK, st.cvM.kJkmolK, st.cpM.kJkmolK, st.w))
            429 3 3737.844 63909.823 235.875 172.283 1891.957 78.673
            """, # Table 10, Pag 842

        "R": 8.314472,
        "cp": Fi2,
        "ref": "NBP",

        "Tmin": Tt, "Tmax": 440.0, "Pmax": 200000.0, "rhomax": 12.3,
        "Pmin": 0.0125, "rhomin": 12.29,

        "nr1": [1.2904, -3.2154, 0.50693, 0.093148, 0.00027638],
        "d1": [1, 1, 1, 3, 7],
        "t1": [0.25, 1.25, 1.5, 0.25, 0.875],

        "nr2": [.71458, .87252, -.015077, -.40645, -.11701, -.13062, -.022952],
        "d2": [1, 2, 5, 1, 1, 4, 2],
        "t2": [2.375, 2, 2.125, 3.5, 6.5, 4.75, 12.5],
        "c2": [1, 1, 1, 2, 2, 2, 3],
        "gamma2": [1]*7}

    eq = helmholtz1, helmholtz2

    _surface = {"sigma": [0.073586, 0.0103, -0.02663],
                "exp": [1.0983, 0.60033, 0.72765]}
    _vapor_Pressure = {
        "eq": 5,
        "ao": [-7.8353, 1.7746, -3.1305,  -3.4216],
        "exp": [1, 1.5, 2.5, 5]}
    _liquid_Density = {
        "eq": 1,
        "ao": [0.463, 2.2375, -0.27579, 0.55136],
        "exp": [0.17, 0.5, 1.3, 2.5]}
    _vapor_Density = {
        "eq": 3,
        "ao": [-0.99583, -2.6109, -4.4141, -18.573, -55.961],
        "exp": [0.24, 0.61, 1, 2.7, 5.95]}

    thermo0 = {"eq": 1,
               "__name__": "Marsh (2002)",
               "__doc__": """Marsh, K., Perkins, R., and Ramires, M.L.V., "Measurement and Correlation of the Thermal Conductivity of Propane from 86 to 600 K at Pressures to 70 MPa," J. Chem. Eng. Data (2002)47(4):932-940""",

               "Tref": 427.16, "kref": 1,
               "no": [0.300728e-1, -0.102742, 0.145703, -0.483106e-1],
               "co": [0, 1, 2, 3],

               "Trefb": 427.16, "rhorefb": 3.85, "krefb": 1,
               "nb": [-0.7391e-2, 0.887221e-2, -0.195198, 0.173498, 0.289485,
                      -.23028, -.126956, .892151e-1, .172567e-1, -.93749e-2],
               "tb": [0, 1]*5,
               "db": [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],
               "cb": [0]*10,

               "critical": 3,
               "gnu": 0.63, "gamma": 1.239, "R0": 1.03,
               "Xio": 0.194e-9, "gam0": 0.0496, "qd": 0.5e-9, "Tcref": 640.80}

    _thermal = thermo0,
