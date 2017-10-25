#!/bin/bash
url=
pass=
username=
mysqldump -u$username -p$pass   -h $url -P 3306 --skip-lock-tables --ignore-table=zyy.message --ignore-table=zyy.cl_dept_relevance --ignore-table=zyy.cl_material --ignore-table=zyy.cl_material_class --ignore-table=zyy.cl_material_unit --ignore-table=zyy.cl_order --ignore-table=zyy.cl_order_detail --ignore-table=zyy.cl_price --ignore-table=zyy.cl_receipt --ignore-table=zyy.cl_receipt_detail --ignore-table=zyy.cl_requisition --ignore-table=zyy.cl_requisition_detail --ignore-table=zyy.cl_return --ignore-table=zyy.cl_return_detail --ignore-table=zyy.cl_stock_count --ignore-table=zyy.cl_stock_count_detail --ignore-table=zyy.cl_stock_transfer --ignore-table=zyy.cl_stock_transfer_detail --ignore-table=zyy.cl_store_relevance --ignore-table=zyy.cl_supplier --ignore-table=zyy.cl_unit --ignore-table=zyy.system_config  zyy >/root/sh/tmp/pre.20171024.sql

mysqldump  -u$username -p$pass  -h $url  -P3306 t_pi >/root/sh/tmp/t_pi.201710-03.sql

