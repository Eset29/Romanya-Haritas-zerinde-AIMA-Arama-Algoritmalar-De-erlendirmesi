Romanya Haritası Üzerinde AIMA Arama Algoritmaları Değerlendirmesi

Çalışmanın AmacıBu 

çalışmada AIMA’nın Search bölümünde tanımlı dört temel arama algoritmasını (DFS-Tree, BFSTree, DFS-Graph, BFS-Graph) Romanya şehir haritası örneği üzerinde uygulayarak; iterasyon sayıları, 
çözüm üretme yetenekleri ve elde edilen yolların optimal olup olmadığı açısından inceledim. Başlangıç noktası 
olarak Arad, hedef nokta olarak Bucharest seçilmiştir.

Sonuçların Özeti:

 DFS-Tree Search: 9 iterasyon sonunda hedefe ulaştı. 
Derinlik öncelikli yapısı nedeniyle Arad→Timisoara→Lugoj→Mehadia→Drobeta→Craiova→Rimnicu 
Vilcea→Pitesti→Bucharest şeklinde uzun ve maliyetli bir yol seçti. Yani çözüm üretmekle birlikte 
maliyet açısından optimal değil. Döngü kontrolü olmadığı için daha karmaşık haritalarda hatalı tekrarlar oluşabilir.
 BFS-Tree Search: 12 iterasyonda hedefe ulaştı. Arad→Sibiu→Fagaras→Bucharest yolu, kenar sayısı bakımından 
en kısa yolu garanti etse de kenar ağırlıkları göz ardı edildiğinden toplam maliyet optimal değil. Buna karşın çözüm 
üretmesi garanti.

 DFS-Graph Search:

9 iterasyonda sonuca vardı. Ziyaret edilen düğümler tutulduğu için döngülerden kaçınabildi. 
Ancak derinlik önceliği yine benzeri uzun bir rota (Arad→Timisoara→…→Bucharest) seçerek maliyet açısından optimal 
olmayan bir sonuç verdi.

 BFS-Graph Search: 

9 iterasyonda hedefe ulaştı. 
Ziyaret kümesi tekrarları engelledi ve Arad→Sibiu→Fagaras→Bucharest yolunu buldu. 
Kenar sayısı açısından optimal ancak maliyet bakış açısından hâlâ global optimum değil. Çözüm üretme garantisi var.

Genel Değerlendirme:

 Tüm algoritmalar verilen senaryoda hedefe ulaşmayı başardı.
 DFS tabanlı yaklaşımlar derinlik önceliği nedeniyle maliyet açısından dezavantajlı sonuçlar üretti.
 BFS tabanlı yaklaşımlar kenar sayısı açısından optimal olduğunu gösterdi ancak ağırlıklı maliyeti göz ardı 
ettikleri için toplam maliyet optimal değil.
 Graf sürümleri, ziyaret edilen düğümleri izleyerek gereksiz tekrarları azalttı ve daha kararlı sonuçlar üretti.
 Romanya örneği üzerinde ek bir harita denemesi yapılmadı; ileride farklı topolojilerle aynı karşılaştırmalar 
yapılabilir.

Sonuç:

Her algoritma hedefe ulaşma bakımından başarılı olsa da gerçek maliyet-optimal çözüm arayışlarında kenar ağırlıklarını 
hesaba katan arama yöntemleri (örneğin UCS veya A) tercih edilmelidir. Bu çalışma, temel arama yaklaşımlarının 
davranışlarını ve güçlü/zayıf yönlerini gözlemlememi sağladı.
