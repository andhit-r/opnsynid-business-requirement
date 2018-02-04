# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Business Requirement - Create Procurement Order "
            "From Resource Lines",
    "summary": "Business Requirement - Create Procurement Order "
            "From Resource Lines",
    "version": "8.0.1.0.0",
    "category": "Business Requirements Management",
    "website": "https://opensynergy-indonesia.com",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "stock",
        "business_requirement_deliverable_cost",
    ],
    "data": [
        "wizards/create_procurement_order_from_resource.xml",
        "views/stock_location_route_views.xml",
        "views/business_requirement_resource_views.xml",
        "views/procurement_order_views.xml",
    ],
}
