def get_model_latex_table(inp):
    zw=[]
    inp.summary(print_fn=lambda x: zw.append(x))
    latex=[]
    nn=0
    for i in range(3,len(zw)-5,2):
        if nn%2 == 0:
            latex.append(r"\rowcolor{my_color!30} $"+zw[i].replace("              ","$ & $")+"$ \\\ \n ")
        else:
            latex.append("$"+zw[i].replace("              ","$ & $")+"$ \\\ \n ")
        nn += 1
    latex.append(" \\\ \n ")
    latex.append(zw[-4]+" \\\ \n ")
    latex.append(zw[-3]+" \\\ \n ")
    latex.append(zw[-2]+" \\\ \n ")
    return latex
        
def model_to_latex(inp,table=False):
    mk_table_str=get_model_latex_table(inp)
    table_str = ''.join(map(str, mk_table_str))
    table_head= r"\begin{tabular}{l  c  r}"+"  \n "+r" \rowcolor{my_color!60} Layer (type) &  Output Shape & Param $N_o$ \\"+" \n "+r" \hline \hline \\"+" \n" 
    table_bottom= " \\ \n \end{tabular} \n"
    begin_fig=r"\begin{figure}[h]"+" \\ \n"+r" \begin{tcolorbox}[colback=my_color!10,colframe=my_color!50!black,fonttitle=\bfseries, title=\scriptsize{Figure~\ref{tab:CHANGE NUMBER}: Model 1}, halign=center]"+"\\ \n"
    end_fig=r"\end{tcolorbox} "+"\\ \n"+" \caption{CHANGE THIS} "+"\\ \n"+r" \label{tab:CHANGE NUMBER} "+"\\ \n"+" \end{figure}"+"\\ \n"
    if table==False:
        out=table_head+table_str+table_bottom
    else:
        out=begin_fig+table_head+table_str+table_bottom+end_fig
    return out 
