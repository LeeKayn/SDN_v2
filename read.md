Tôi sẽ giải thích chi tiết về cách các thông số chuẩn hóa giúp phát hiện tấn công DDoS:

1. speed_src_ip (Tốc độ gói tin từ IP nguồn):
- Trong tấn công DDoS, kẻ tấn công thường gửi một lượng lớn gói tin trong thời gian ngắn
- Khi tính tốc độ = số gói tin/thời gian, giá trị này sẽ cao bất thường trong trường hợp DDoS
- Traffic bình thường sẽ có tốc độ gói tin ổn định và thấp hơn

2. std_n_packets (Số lượng gói tin chuẩn hóa):
- Chuẩn hóa giúp so sánh với mức trung bình và độ lệch chuẩn của traffic bình thường
- Trong DDoS, số lượng gói tin sẽ cao hơn nhiều so với bình thường
- Sau khi chuẩn hóa, các giá trị bất thường sẽ nổi bật hơn

3. std_bytes (Kích thước byte chuẩn hóa):
- DDoS có thể gửi nhiều gói tin nhỏ hoặc lớn để tăng tải
- Chuẩn hóa byte count giúp phát hiện những bất thường về kích thước gói tin
- Có thể phát hiện cả tấn công flood gói tin nhỏ và tấn công với gói tin lớn

4. bytes_per_flow (Byte trên mỗi luồng):
- Một flow là một phiên kết nối giữa source và destination
- DDoS thường có nhiều flow ngắn với ít byte/flow
- Traffic bình thường có số byte/flow ổn định hơn

5. n_int_flows (Số lượng flow được chuẩn hóa):
- DDoS tạo ra nhiều flow giả mạo trong thời gian ngắn
- Tỷ lệ flow/số gói tin sẽ bất thường trong DDoS
- Traffic hợp lệ có tỷ lệ này ổn định hơn

Về cách thu thập dữ liệu:

1. Port lắng nghe (Listen Port):
- Switch/Router sẽ có các port mirror hoặc span port để theo dõi traffic
- Các công cụ như Wireshark, tcpdump có thể capture packet từ các port này
- Netflow/sFlow cũng có thể thu thập thống kê về luồng traffic

2. Quá trình thu thập:
```
[Traffic] -> [Switch/Router] -> [Mirror Port] -> [Network Monitor] -> [Feature Extraction]
```

3. Các thông số được tính toán:
- Số packet và byte được đếm trực tiếp từ traffic
- Thời gian được tính từ timestamp của gói tin
- Flow được xác định dựa trên source IP, dest IP, protocol
- Các metric khác được tính toán từ các thông số cơ bản trên

4. Lợi ích của việc chuẩn hóa:
- Loại bỏ sự khác biệt về scale giữa các features
- Dễ dàng so sánh và phát hiện bất thường
- Cải thiện hiệu quả của các thuật toán ML
- Giảm ảnh hưởng của outlier

Ví dụ về traffic bình thường vs DDoS:

```python
# Traffic bình thường
normal = {
    'speed_src_ip': 100-200,      # Packets/sec
    'bytes_per_flow': 1000-5000,  # Bytes/flow
    'n_int_flows': 0.001-0.01     # Flows/packet
}

# Traffic DDoS
ddos = {
    'speed_src_ip': 1000+,        # Rất nhiều packets/sec
    'bytes_per_flow': 50-100,     # Ít bytes/flow
    'n_int_flows': 0.1+           # Nhiều flows/packet
}
```

Khi phát hiện các giá trị bất thường trong các metric này, hệ thống có thể cảnh báo về khả năng xảy ra tấn công DDoS. Việc kết hợp nhiều metric giúp giảm false positive và tăng độ chính xác trong việc phát hiện tấn công.