# -*- coding: utf-8 -*-
"""
/***************************************************************************
 CPR
                                 A QGIS plugin
 CPR (Colour Pattern Regression)
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2022-05-16
        copyright            : (C) 2022 by Vielca Ingenieros
        email                : pep.j@vielca.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load CPR class from file CPR.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .CPR import CPR
    return CPR(iface)
