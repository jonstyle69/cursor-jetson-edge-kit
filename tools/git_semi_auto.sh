#!/usr/bin/env bash
# 半自動 Git 提交流程（安全檢查版）
# 使用方式：在專案根目錄執行： bash tools/git_semi_auto.sh

set -e

echo "==============================="
echo "  Jetson x Cursor Git 半自動流程"
echo "==============================="
echo

echo "[1/5] 目前 Git 狀態："
git status
echo

read -p "是否要將所有變更加入暫存區 (git add .) ? [y/N]: " ADD_ALL
if [[ "$ADD_ALL" == "y" || "$ADD_ALL" == "Y" ]]; then
  git add .
  echo "已執行：git add ."
else
  echo "未自動 add，請自行 git add 後再重跑腳本。"
  exit 0
fi

echo
echo "[2/5] 已加入暫存區的檔案："
git diff --cached --name-only || true
echo

echo "[3/5] 安全檢查：是否有敏感或大檔案被加入？"

SENSITIVE_PATTERNS='(\.env$|\.key$|\.pem$|^models/|^data_raw/|^dataset/|\.onnx$|\.engine$|\.tflite$|\.pt$|\.pth$)'
STAGED_SENSITIVE=$(git diff --cached --name-only | grep -E "$SENSITIVE_PATTERNS" || true)

if [[ -n "$STAGED_SENSITIVE" ]]; then
  echo "⚠ 發現以下『可能不該上傳』的檔案已加入暫存區："
  echo "$STAGED_SENSITIVE"
  echo
  echo "請執行例如： git restore --staged <檔名>  將它們從暫存區移除後再重跑腳本。"
  exit 1
else
  echo "✔ 安全檢查通過，沒有偵測到 .env / models / dataset 等敏感檔案。"
fi

echo
echo "[4/5] 準備 commit。"
echo "建議做法：可以請 Cursor 幫你產生一段 commit message，然後貼到這裡。"
read -p "請輸入 commit 訊息（例如：feat(camera): 支援 USB/MIPI 切換）: " COMMIT_MSG

if [[ -z "$COMMIT_MSG" ]]; then
  echo "未輸入訊息，改用預設訊息：chore: update"
  COMMIT_MSG="chore: update"
fi

git commit -m "$COMMIT_MSG"
echo "✔ 已完成 commit。"
echo

read -p "[5/5] 是否要將本次 commit push 到遠端？ [y/N]: " DO_PUSH
if [[ "$DO_PUSH" == "y" || "$DO_PUSH" == "Y" ]]; then
  echo "執行：git push"
  git push
  echo "✔ 已 push 到遠端。"
else
  echo "本次 commit 尚未 push，你之後可自行執行：git push"
fi

echo
echo "🎉 Git 半自動流程結束。"

