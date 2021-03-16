# keras_model_latex

load keras
```python
import keras
from keras.models import Model
from keras.layers import Input,Dense
from keras import Sequential
```

setup model
```python
model=Sequential()
model.add(Dense(512,input_shape=(2303,),activation='linear'))
model.add(Dense(2048,activation='relu'))
model.add(Dense(512,activation='sigmoid'))
model.add(Dense(16,activation='linear'))
model.add(Dense(1,activation='linear'))
```

get layers
```python
model_summary=model.summary()
```

    _________________________________________________________________
    Layer (type)                 Output Shape              Param #   
    =================================================================
    dense_1 (Dense)              (None, 512)               1179648   
    _________________________________________________________________
    dense_2 (Dense)              (None, 2048)              1050624   
    _________________________________________________________________
    dense_3 (Dense)              (None, 512)               1049088   
    _________________________________________________________________
    dense_4 (Dense)              (None, 16)                8208      
    _________________________________________________________________
    dense_5 (Dense)              (None, 1)                 17        
    =================================================================
    Total params: 3,287,585
    Trainable params: 3,287,585
    Non-trainable params: 0
    _________________________________________________________________


load functions from keras_latex.py
```python
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
        
```

get the code for ![latex table](https://github.com/ambader/keras_model_latex/blob/main/latex_table.pdf)

```python
latex_table=model_to_latex(model)
```
<img src="https://user-images.githubusercontent.com/42641926/111282970-dc79db80-863e-11eb-8964-810e7807c2b8.png" width="250" border="1">

or

get the code for ![latex figure](https://github.com/ambader/keras_model_latex/blob/main/latex_figure.pdf)
```python
latex_figure=model_to_latex(model,True)
```
<img src="https://user-images.githubusercontent.com/42641926/111282466-52317780-863e-11eb-91e0-15b3e8acff54.png" width="250" border="1">

save code in txt file
```python
with open('latex_table.txt','w') as f:
    f.write(latex_table)
f.close()
```
