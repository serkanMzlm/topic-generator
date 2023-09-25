## ROS2'da Param Dosyasından Topic Oluşturma
Paketin içinde bulunan `params\topic_names.yml` dosyası ROS2 için **publications** ve **subscriptions** içerir. Bu dosyaya doğru bir şekilde yazılan paket ROS2 tarafında bulunan paketi günceller. Bu sayede sadece param tarafında ekleme yaparak ROS2 tarafında yeni publisher ve subscriber üretmesini sağlar. 

#### Build
```
colcon build --packages-select dynamic_topic
```