# TGneuralODE

Para instalar:
```
pip install git+https://github.com/rtqichen/torchdiffeq
```

As duas bases de dados estão disponíveis em:

UFPR-ALPR: (https://web.inf.ufpr.br/vri/databases/ufpr-alpr/)

UFPR-AMR: (https://web.inf.ufpr.br/vri/databases/ufpr-amr/)

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
 
