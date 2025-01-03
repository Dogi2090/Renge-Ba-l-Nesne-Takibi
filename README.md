# Nesne Takibi ve Hareket Yolu Görselleştirme

Bu proje, kameradan alınan görüntülerdeki **yeşil renkteki nesneleri** tespit ederek, nesnenin hareket yolunu takip etmeyi ve bu yolu görselleştirmeyi amaçlamaktadır.

## Gereksinimler

Bu projeyi çalıştırabilmek için aşağıdaki kütüphaneler gereklidir:

- `opencv-python` (cv2): Görüntü işleme ve kameradan video akışı için.
- `numpy`: Sayısal hesaplamalar ve veri manipülasyonu için.
- `matplotlib`: Nesne hareketinin görselleştirilmesi için.

Gerekli kütüphaneleri yüklemek için aşağıdaki komutu çalıştırabilirsiniz:
pip install opencv-python numpy matplotlib

## Kurulum ve Kullanım

1. **Kodun Çalıştırılması:**

   Bu Python kodunu çalıştırarak kamera üzerinden gerçek zamanlı nesne takibi yapabilirsiniz. Kod, yeşil renkteki nesneleri tespit eder ve hareketini takip eder.

   - Kameranızın doğru şekilde bağlı olduğundan emin olun.
   - Kod çalıştığında, yeşil renk aralığındaki nesneler ekranda takip edilecektir.
   - Hareket eden nesnelerin merkez noktaları ekranda gösterilecek ve hareket yolu görselleştirilecektir.

2. **Çalıştırma:**

   Aşağıdaki komutu çalıştırarak Python dosyasını başlatabilirsiniz:
   python nesne_takibi.py

Program çalıştıktan sonra, kamera görüntüsünde yeşil nesneler takip edilmeye başlanacaktır.

3. **Çıkış Yapma:**

Takip edilen nesne verilerini kaydettikten sonra programdan çıkmak için **'q'** tuşuna basmanız yeterlidir.

4. **Sonuçların Görselleştirilmesi:**

Takip edilen nesnenin hareket yolu, ekranın sonunda bir grafik olarak gösterilecektir. Bu grafik, nesnenin x ve y koordinatlarını zamanla takip eder.

## Kod Açıklaması

- **HSV Renk Uzayı**: Kod, görüntüyü HSV renk uzayına çevirir ve yeşil renk aralığını tespit eder. Yeşil renkli nesneleri maskeleme işlemi yapılır.

- **Kontur Tespiti**: Maskedeki konturlar bulunur ve en büyük konturlar (belirli bir alanın üzerindeki) takip edilir.

- **Hareket Yolu**: Nesnenin merkezi her çerçeve için hesaplanır ve hareket yolu boyunca bu noktalar kaydedilir.

- **Ekran Üzerinde Görselleştirme**: Nesnenin merkezini temsil eden daire ekranda görünür. Ayrıca nesnenin (x, y) koordinatları ekranda yazdırılır.

## Sorun Giderme

- **Kamera Erişimi**: Eğer kamera açılmıyorsa, bilgisayarınızın kamera ayarlarını kontrol edin. Diğer uygulamalar tarafından kameranın kullanılıp kullanılmadığını kontrol edin.

- **Yeşil Nesnelerin Takibi**: Kodda tanımlanan yeşil renk aralığı (HSV: [40, 40, 40] ile [80, 255, 255]) çok dar olabilir. Eğer başka renklerde nesneleriniz varsa, bu aralığı değiştirebilirsiniz.

Örnek olarak:

```python
lower_green = np.array([30, 50, 50])  # Daha geniş bir yeşil aralığı
upper_green = np.array([90, 255, 255])

