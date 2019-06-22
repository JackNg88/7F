#go_gene_map.py
from glbase import *
import os
import csv
os.chdir('/Users/wuxiaojian/wujian/4_liujing/6_ATAC_GO_heatmap/1_per_align')
expn = glload('../0_datas/mgi_go.glb')
#print expn


gos = ['GO:0002685', 'GO:0060348', 'GO:0007596', 'GO:0045598', 'GO:0071559', 'GO:0008154', 'GO:0030042', 'GO:0031099', 'GO:0051099', 'GO:0051216', 'GO:0072089', 'GO:0043406', 'GO:0045216', 'GO:0014812', 'GO:0072091', 'GO:0048754', 'GO:0043122', 'GO:0050679', 'GO:0010810', 'GO:0048864', 'GO:0014909', 'GO:0060401', 'GO:0032845', 'GO:0048659', 'GO:0007160', 'GO:0016331', 'GO:0050774', 'GO:0046578', 'GO:0009636', 'GO:2000648', 'GO:0048704', 'GO:0043542', 'GO:0045667', 'GO:0097192', 'GO:0010632', 'GO:0071425', 'GO:0010812', 'GO:0001894', 'GO:0010594', 'GO:2000738', 'GO:0045740', 'GO:2000736', 'GO:0060491', 'GO:0031334', 'GO:0001953', 'GO:0090183', 'GO:0006346', 'GO:0018022', 'GO:0044728', 'GO:0016571', 'GO:0001825', 'GO:0001824', 'GO:0003401', 'GO:0072172', 'GO:0001708', 'GO:2000737', 'GO:0019827', 'GO:0033048', 'GO:0010948']
#expn[0]
#go = 'GO:0071559'

for go in gos:
    print go
    data = []
    for item in expn:
        #print item  #{'GO_id': 'GO:0003674', 'MGI_id': 'MGI:1918911', 'name': '0610005C13Rik'}
        if go in item.values():  #['MGI:1918911', '0610005C13Rik', 'GO:0003674']
            #print go
            data.append(item.values())
    
    go = go[:2] + '_' + go[3:]
    csvfile = file(name = '%s.tsv' % go, mode='wb')
    writer = csv.writer(csvfile, dialect= csv.excel_tab)
    writer.writerow(['MGI_id', 'name', 'GO_id'])
    writer.writerows(data)
    csvfile.close()    
    #bad 

print 'good jobs'
