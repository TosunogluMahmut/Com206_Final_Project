using System;
using System.Collections.Generic;

namespace Com_206Project
{
    // Çekici bilgilerini tutan sınıf (Class)
    class Cekici
    {
        public string Plaka { get; set; }
        public string SurucuIsmi { get; set; }
        public string AracTipi { get; set; } // Kayar kasa, Ahtapot vb.
        public bool MusaitMi { get; set; }

        public Cekici(string plaka, string isim, string tip)
        {
            Plaka = plaka;
            SurucuIsmi = isim;
            AracTipi = tip;
            MusaitMi = true;
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            List<Cekici> filo = new List<Cekici>();
            
            // Başlangıç için seni sisteme ekleyelim
            filo.Add(new Cekici("34 GEL 2026", "Mahmut Eren", "Kayar Kasa"));

            while (true)
            {
                Console.Clear();
                Console.WriteLine("======================================");
                Console.WriteLine("   COM-206 YOL YARDIM TAKİP SİSTEMİ   ");
                Console.WriteLine("======================================");
                Console.WriteLine("1 - Yeni Çekici Kaydet");
                Console.WriteLine("2 - Tüm Filoyu Listele");
                Console.WriteLine("3 - Çıkış");
                Console.Write("\nSeçiminiz: ");

                string secim = Console.ReadLine();

                if (secim == "1")
                {
                    Console.Write("Plaka Giriniz: "); string p = Console.ReadLine();
                    Console.Write("Sürücü İsmi: "); string s = Console.ReadLine();
                    Console.Write("Araç Tipi (Örn: Kayar Kasa): "); string t = Console.ReadLine();
                    
                    filo.Add(new Cekici(p, s, t));
                    Console.WriteLine("\nKayıt Başarılı! Devam etmek için bir tuşa basın...");
                    Console.ReadKey();
                }
                else if (secim == "2")
                {
                    Console.WriteLine("\n--- Mevcut Kayıtlı Araçlar ---");
                    if (filo.Count == 0) Console.WriteLine("Sistemde araç bulunamadı.");
                    
                    foreach (var c in filo)
                    {
                        string durum = c.MusaitMi ? "MÜSAİT" : "GÖREVDE";
                        Console.WriteLine($"-> [{c.Plaka}] | Sürücü: {c.SurucuIsmi} | Tip: {c.AracTipi} | Durum: {durum}");
                    }
                    Console.WriteLine("\nMenüye dönmek için bir tuşa basın...");
                    Console.ReadKey();
                }
                else if (secim == "3")
                {
                    Console.WriteLine("Sistem kapatılıyor...");
                    break;
                }
            }
        }
    }
}