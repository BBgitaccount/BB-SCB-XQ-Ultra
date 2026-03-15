# Windows Bluetooth Audio Optimizer (SBC-XQ Ultra)

![table.png](C:\Users\THINKPAD\Desktop\table.png)

## 1. Overview & Analytical Gains

This tool modifies Windows kernel-level Bluetooth stack parameters to force the high-bitrate SBC-XQ protocol. It maximizes the `BTHPORT` bitpool capacity and disables lower-bandwidth codecs (`AAC`/`aptX`) to prevent automatic fallback during the hardware handshake.

| **Metric**       | **Default Windows (AAC/aptX)** | **Optimized System (SBC-XQ)** | **Bandwidth Gain** |
| ---------------- | ------------------------------ | ----------------------------- | ------------------ |
| **Active Codec** | AAC / aptX                     | SBC                           | N/A                |
| **Max Bitrate**  | ~256 kbps / ~352 kbps          | **~664 kbps**                 | **+88% to +159%**  |
| **Sample Rate**  | 44.1 kHz / 16-bit              | 44.1 kHz / 16-bit             | Constant           |

## 2. Execution Instructions

To apply the kernel parameters:

1. Right-click `run_optimizer.bat`.

2. Select **Run as administrator** (Mandatory for registry modification).

3. **Reboot** the operating system to load the new stack parameters.

## 3. Rollback Procedure

If hardware incompatibility, audio stuttering, or latency issues occur, restore the factory defaults:

1. Right-click `undo.bat`.

2. Select **Run as administrator**.

3. **Reboot** the operating system to restore the original Windows codec selection algorithm.

---

BB
