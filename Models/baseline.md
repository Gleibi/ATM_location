# Решение задачи регрессии

В данной задаче регрессии в качестве бейзлайна используется **константная медиана**, поскольку целевое значение очень сильно меняется и имеет множество выбросов.

---

## Модели и их результаты

### Линейная регрессия
- **MSE:** 0.005208636414630403  
- **RMSE:** 0.0721708834269777  
- **R²:** 0.31390183316626574  

---

### Lasso Regression
- **MSE:** 0.0075916820236393585  
- **RMSE:** 0.08713025894394759  
- **R²:** -5.193246293000442e-07  

> _Далее я везде пользовался подбором гиперпараметров._

#### Результаты на тестовой выборке для лучшей модели Lasso:
- **MSE:** 0.005206325419086802  
- **RMSE:** 0.07215487106971227  
- **R²:** 0.31420624485481663  

#### Результаты на тестовой выборке для лучшей модели Ridge:
- **MSE:** 0.005210827797467809  
- **RMSE:** 0.07218606373440659  
- **R²:** 0.3136131772440838  

#### Результаты на тестовой выборке для лучшей модели ElasticNet:
- **MSE:** 0.005206282368497156  
- **RMSE:** 0.07215457274835155  
- **R²:** 0.3142119156155083  

---

### Добавление One-Hot Encoding (OHE)

После применения OHE кодирования для категориальных признаков:

#### Результаты на тестовой выборке для ElasticNet с OHE:
- **MSE:** 0.002274398708631506  
- **RMSE:** 0.047690656408058654  
- **R²:** 0.7004089630334052  

---

### Решающие деревья

#### Decision Tree Regressor Performance:
- **MSE:** 0.003533970363629737  
- **RMSE:** 0.05944720652503141  
- **R²:** 0.5344941756117647  

#### Результаты на тестовой выборке для лучшей модели RandomForestRegressor:
- **MSE:** 0.0021308960016955965  
- **RMSE:** 0.046161629105736686  
- **R²:** 0.7193115963383241  

---

### Бустинг модели

#### Результаты на тестовой выборке для лучшей модели CatBoostRegressor:
- **MSE:** 0.002058849034883391  
- **RMSE:** 0.0453745417043896  
- **R²:** 0.7288018521213806  

#### Результаты на тестовой выборке для лучшей модели XGBRegressor:
- **MSE:** 0.0020574162928616306  
- **RMSE:** 0.04535875100641144  
- **R²:** 0.7289905774606872  

---

## Выбор лучших моделей

В итоге были выбраны две лучшие модели:
1. **Лучшая линейная модель:** ElasticNet с OHE  
2. **Лучшая модель в абсолюте:** XGBRegressor

> **Примечание:** Среди ключевых признаков сильно превалировала информация о том, к какому банку принадлежит банкомат. Если обучать модель без этой информации, результат значительно ухудшается.

