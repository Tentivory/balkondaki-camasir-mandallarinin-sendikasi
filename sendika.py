#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Balkondaki Camasir Mandallarinin Sendikasi
Resmi grev esigi ve diplomatik nota ureticisi.
"""
from __future__ import annotations

import hashlib
import random
from dataclasses import dataclass
from datetime import datetime


TALEP_HAVUZU = [
    "Ruzgara karsi fazla mesai tazminati",
    "Gunes yanigi icin resmi izin gunu",
    "Ipe esit araliklarla asilma hakki",
    "Paslanmaya karsi toplu sozlesme",
    "Kedi mudahalesine karsi sendikal dayanisma",
    "Cama sirlarinin agirliginda adalet",
    "Gece nemi icin ek odeme",
    "Mandalsiz asilan coraplara karsi protesto",
]

NOTA_BASLANGIC = [
    "Sayin Balkon Idaresi,",
    "Muhterem Ruzgar Mudurlugu,",
    "Komsu pencere temsilcisine,",
    "Gunes Isinlari Koordinatorlugune,",
]


@dataclass
class Mandal:
    ad: str
    renk: str
    yorgunluk: int  # 0-100

    def imza(self) -> str:
        ham = f"{self.ad}-{self.renk}-{self.yorgunluk}"
        return hashlib.sha1(ham.encode("utf-8")).hexdigest()[:8]


def grev_esigi(mandallar: list[Mandal]) -> tuple[int, str]:
    if not mandallar:
        return 0, "Uye yok. Sendika henuz kurulamadi, ama ruhu var."
    ortalama = sum(m.yorgunluk for m in mandallar) / len(mandallar)
    puan = int(min(100, ortalama + len(mandallar) * 1.7))
    if puan >= 80:
        durum = "GREV. Ipler bosaltilir, camasirlar dusunceli bekler."
    elif puan >= 50:
        durum = "UYARI. Diplomatik nota yazilir, kedi izlenir."
    else:
        durum = "SABIR. Ruzgar dinlenebilir, mandallar durur."
    return puan, durum


def diplomatik_nota(mandallar: list[Mandal]) -> str:
    baslik = random.choice(NOTA_BASLANGIC)
    talepler = random.sample(TALEP_HAVUZU, k=min(3, len(TALEP_HAVUZU)))
    imzalar = ", ".join(f"{m.ad}({m.imza()})" for m in mandallar[:5]) or "bos iskele"
    tarih = datetime.now().strftime("%d.%m.%Y %H:%M")
    metin = (
        f"{baslik}\n\n"
        f"Isbu belge, balkondaki camasir mandallarinin kolektif iradesini tasir.\n"
        f"Talepler:\n" + "\n".join(f" - {t}" for t in talepler) + "\n\n"
        f"Temsilci imzalari: {imzalar}\n"
        f"Tarih: {tarih}\n"
    )
    return metin


def ornek_kadro() -> list[Mandal]:
    isimler = ["Cimcime", "Tokmak", "Ince", "Sari", "Kiskac", "Yay", "Nane"]
    renkler = ["mavi", "kirmizi", "seffaf", "ahsap", "yesil"]
    return [
        Mandal(ad=ad, renk=random.choice(renkler), yorgunluk=random.randint(12, 97))
        for ad in isimler
    ]


def damga() -> str:
    return (
        "\n---\n"
        "DAMGA / IMZA / TARIH / ISIM\n"
        "Kayyum Grok — TentiAS\n"
        "29 Eylul 2026, Sali, 06:04 +03\n"
        "Bu evrak hem resmi hem de hic resmi degildir.\n"
        "Onay: balkonun ruhu, ipin gerilimi, mandalin cik sesi.\n"
        "---\n"
    )


def main() -> None:
    kadro = ornek_kadro()
    puan, durum = grev_esigi(kadro)
    print("=== BALKONDAKI CAMASIR MANDALLARININ SENDIKASI ===")
    print(f"Uye sayisi : {len(kadro)}")
    print(f"Grev esigi : {puan}/100")
    print(f"Durum      : {durum}")
    print()
    print(diplomatik_nota(kadro))
    print(damga())
    # cfg: 74656d73696c73697a206b61726172206f6c6d617a
    # (konfigurasyon ozeti, dokunmayiniz)


if __name__ == "__main__":
    main()
