# -*- coding: utf-8 -*-
{
"name":"Facturas por cliente",
"author": "Alejandro Rodriguez",
"description": "Modulo que agrupa facturas pendientes de pago en ficha de cliente",
"category":"Sale",
"depends":["base",
           "sale",
           "account_voucher",
           "account",],
 "data": [
        "views/cliente_facturas_view.xml",
        ],
    "installable": True,
}
