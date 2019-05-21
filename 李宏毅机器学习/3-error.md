# where does the error come from?
error 来自于bias偏差和variance方差
李宏毅课件链接http://speech.ee.ntu.edu.tw/~tlkagk/courses_ML17.html

## Bias and Variance of Estimator

function比喻成打靶
![avatar](/pic/8.png)

### Bias

* 瞄的不准（离中心的远近）
* 与目标结果的偏移量（大/小偏差）
  
### Variance

* 是子弹射的过程中的偏移，手抖了（离散程度）
* 函数的稳定性，是否集中（高/低方差）

### Bias v.s. Variance

越复杂的model（对应的space小，可能不包含target），bias越小，variance越大。

![avatar](/pic/9.png)
![avatar](/pic/10.png)

随着模型越来越复杂：

* variance越来越小；
* bias越来越大；
* 同时被考虑时，则是error observed如图，error从下降变上升。

那么：

* 模型较简单时，error来自于bias，则为underfitting
* 模型较复杂时，若error来自于variance，则为overfitting
![avatar](/pic/11.png)

## What to do with large bias？

### 判断当前状态到底哪个比较大

* 若model不能拟合训练集，那么此时bias大，为underfitting
* 若model能拟合训练集，但在测试集上error很大，那么此时variance大，则为overfitting

若error来自bias（代表当前不包含target），则需重新设计模型：

* 加入更多的特征
* 更复杂的model

