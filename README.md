# TGneuralODE

Para instalar:
```
pip install git+https://github.com/rtqichen/torchdiffeq
```

As duas bases de dados estão disponíveis em:

UFPR-ALPR: (https://drive.google.com/file/d/154f5NALWysmhXmrWnNUjjnd4IrME2cpS/view?usp=sharing)

UFPR-AMR: (https://drive.google.com/file/d/1ewH_x58NaG3joEy4SeKc3gAON6LstYnM/view?usp=sharing)

- Extrair as bases de dados no respectivo diretório

## Base MNIST:

 ResNet: 
 ```
 python3 odenet_mnist.py --network resnet --adjoint False --downsampling-method res
 ```
 Neural ODE: 
 ```
 python3 odenet_mnist.py --network odenet --adjoint True
 ```

## Base UFPR-AMR:
```
python3 cropmeter.py
resize-script.sh
``` 
 ResNet: 
 ```
 python3 odenet_meter.py --network resnet --adjoint False --downsampling-method res 
 ```
 Neural ODE: 
 ```
 python3 odenet_meter.py --network odenet --adjoint True 
 ```
## Base UFPR-ALPR:
Para base original: 
```
python3 cropplaca.py
resize-script.sh
```
Para data augmentation: 
```
python3 dataaugm.py
resize-script.sh
```
 ResNet: 
 ```
 python3 odenet_placas.py --network resnet --adjoint False --downsampling-method res 
 ```
 Neural ODE: 
 ```
 python3 odenet_placas.py --network odenet --adjoint True 
 ```
 
 ### Para outros parâmetros de execução, consultar os códigos-fonte
 
