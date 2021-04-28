---
# Front matter
lang: ru-RU
title: "Лабораторная №5"
subtitle: "Задача об эпидемии"
author: "Игнатьев Николай"

# Formatting
toc-title: "Содержание"
toc: true # Table of contents
toc_depth: 2
lof: false # List of figures
lot: false # List of tables
fontsize: 12pt
linestretch: 1.5
papersize: a4paper
documentclass: scrreprt
polyglossia-lang: russian
polyglossia-otherlangs: english
mainfont: PT Serif
romanfont: PT Serif
sansfont: PT Sans
monofont: PT Mono
mainfontoptions: Ligatures=TeX
romanfontoptions: Ligatures=TeX
sansfontoptions: Ligatures=TeX,Scale=MatchLowercase
monofontoptions: Scale=MatchLowercase
indent: true
pdf-engine: lualatex
header-includes:
  - \linepenalty=10 # the penalty added to the badness of each line within a paragraph (no associated penalty node) Increasing the value makes tex try to have fewer lines in the paragraph.
  - \interlinepenalty=0 # value of the penalty (node) added after each line of a paragraph.
  - \hyphenpenalty=50 # the penalty for line breaking at an automatically inserted hyphen
  - \exhyphenpenalty=50 # the penalty for line breaking at an explicit hyphen
  - \binoppenalty=700 # the penalty for breaking a line at a binary operator
  - \relpenalty=500 # the penalty for breaking a line at a relation
  - \clubpenalty=150 # extra penalty for breaking after first line of a paragraph
  - \widowpenalty=150 # extra penalty for breaking before last line of a paragraph
  - \displaywidowpenalty=50 # extra penalty for breaking before last line before a display math
  - \brokenpenalty=100 # extra penalty for page breaking after a hyphenated line
  - \predisplaypenalty=10000 # penalty for breaking before a display
  - \postdisplaypenalty=0 # penalty for breaking after a display
  - \floatingpenalty = 20000 # penalty for splitting an insertion (can only be split footnote in standard LaTeX)
  - \raggedbottom # or \flushbottom
  - \usepackage{float} # keep figures where there are in the text
  - \floatplacement{figure}{H} # keep figures where there are in the text
---

# Цель работы
Цель работы -- рассмотреть простейшую модель эпидемии. Исследовать разницу развития эпидемии в случаях преодоления
порогового значения в начале эпидемии и в противном случае.

# Задание
Смоделировать "эпидемию со следующими значениями":

- Число жителей(N) = 17854
- Число заболевших в самом начале(I(0)) = 199
- Число людей с иммунитетом в самом начале(R(0)) = 35

Придумать коэффициенты и изучить поведение при I(0) > I* и в противном случае.

# Выполнение лабораторной работы
Всего в модели два коэффициента a отвечает за скорость заражения, а b за скорость выздоровления. 
Первые результаты были получены для конфигурации a = 0.2, b = 0.1. При таких коэффициентах в зависимости от критического
значения либо абсолютно все люди переболели, либо никто кроме начальных инфицированных не заражался.
![График 1](../source/lab05_bad.png)
![График 2](../source/lab05_good.png)
Однако при значениях b значительно превосходящих a может возникнуть ситуация в которой не все люди переболеют во время эпидемии.
![График 3](../source/lab05_mean.png)

# Выводы
В ходе работы были исследованы модели эпидемий, найдены различные варианты их развития.
