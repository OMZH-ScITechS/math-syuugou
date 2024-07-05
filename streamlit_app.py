import streamlit as st
import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn2_circles
import numpy as np

def main():
    st.title("集合を求める")

    # 入力フォーム
    U = st.text_input("全体集合を入力してください")
    A = st.text_input("集合Aを入力してください")
    B = st.text_input("集合Bを入力してください")

    # 空の場合は空集合として扱う
    zentaisyuugouu = set(U.split()) if U else set()
    syuugoua = set(A.split()) if A else set()
    syuugoub = set(B.split()) if B else set()

    # 集合演算
    katu = syuugoua & syuugoub   # AかつB
    mataha = syuugoua | syuugoub # AまたはB
    a_barkatu = (zentaisyuugouu - syuugoua) & syuugoub    # AバーかつB
    a_barmataha = (zentaisyuugouu - syuugoua) | syuugoub  # AバーまたはB
    b_barkatu = (zentaisyuugouu - syuugoub) & syuugoua    # AかつBバー
    b_barmataha = (zentaisyuugouu - syuugoub) | syuugoua  # AまたはBバー
    a_barkatub_bar = (zentaisyuugouu - syuugoua) & (zentaisyuugouu - syuugoub)  # AバーかつBバー
    a_barmataha_bar = (zentaisyuugouu - syuugoua) | (zentaisyuugouu - syuugoub)  # AバーまたはBバー

    # 結果の表示
    st.write("AかつB:", katu)
    st.write("AまたはB:", mataha)
    st.write("ＡバーかつＢ:", a_barkatu)
    st.write("ＡバーまたはＢ:", a_barmataha)
    st.write("ＡかつＢバー:", b_barkatu)
    st.write("ＡまたはＢバー:", b_barmataha)
    st.write("ＡバーかつＢバー:", a_barkatub_bar)
    st.write("ＡバーまたはＢバー:", a_barmataha_bar)

    # ベン図の作成と表示
    plt.figure(figsize=(8, 6))
    v = venn2(subsets=(len(syuugoua - syuugoua & syuugoub), len(syuugoub - syuugoua & syuugoub), len(syuugoua & syuugoub)), set_labels=('A', 'B'))
    venn2_circles(subsets=(len(syuugoua), len(syuugoub), len(syuugoua & syuugoub)))
    plt.title("ベン図")  # ベン図のタイトルを設定

    # 注釈を追加
    plt.annotate('AかつB', xy=v.get_label_by_id('10').get_position() - np.array([0, 0.05]), xytext=(-70,-70),
                 ha='center', textcoords='offset points', bbox=dict(boxstyle='round,pad=0.5', fc='gray', alpha=0.1),
                 arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.5',color='gray'))
    plt.annotate('AまたはB', xy=v.get_label_by_id('01').get_position() - np.array([0, 0.05]), xytext=(70,-70),
                 ha='center', textcoords='offset points', bbox=dict(boxstyle='round,pad=0.5', fc='gray', alpha=0.1),
                 arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=-0.5',color='gray'))

    plt.tight_layout()

    # ベン図を画像として表示
    st.pyplot(plt)

if __name__ == "__main__":
    main()
