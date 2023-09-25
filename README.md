## ROS2'da Param Dosyasından Topic Oluşturma
Paketin içinde bulunan `params\topic_names.yml` dosyası ROS2 için **publications** ve **subscriptions** içerir. Bu dosyaya doğru bir şekilde yazılan paket ROS2 tarafında bulunan paketi günceller. Bu sayede sadece param tarafında ekleme yaparak ROS2 tarafında yeni publisher ve subscriber üretmesini sağlar. 

#### Build
```
colcon build --packages-select dynamic_topic
```
#### Run
```
. install/setup.bash
ros2 run dynamic_topic dynamic_topic_node
```

- `main.cpp` dosyasına eklenmek istenen yeni özellikler yazılır.
- `dynamic_topic.cpp` ve `dynamic_topic.hpp` dosyalarına kalıcı bir kod yazılması için bu dosyaların `.em` uzantılı paketlerine yazılmalıdır. (Bu dosyalar sürekli baştan oluşturulduğu için bu dosyalara yazdığınız kodlar geçersiz olur.)
- Eklenen yeni dosya veya silinen yeni dosya sonucunda hata alma durumunda **build, log, install** klasörleri silinip tekrardan build işlemi yapılmalıdır.

- `dynamic_topic.cpp` dosyasında bulunan `(void)msg` kısımları sadece uyarılardan kurtulmak için yazılmıştır.