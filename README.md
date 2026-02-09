# SIGET: Process Scheduling and Concurrency Simulator
Project Overview
This project involves the design and implementation of a CPU Scheduling Simulator and a Concurrency Control Module for the SIGET (Intelligent Traffic Management System). The goal is to optimize urban mobility by managing routine traffic data and high-priority emergency alerts through efficient resource orchestration.
Key Features
1. CPU Scheduler Simulator
The system acts as a "silent architect," coordinating every action within the device to prevent system collapse.
• Scheduling Algorithms:
    ◦ Priority Scheduling: Inspired by the Harvard architecture, it prioritizes critical signals (e.g., ambulances) to eliminate bus latency and overhead, ensuring immediate real-time response.
    ◦ Round-Robin: Ensures equitable processing of routine traffic data, allowing multiple applications to coexist without a single task monopolizing the CPU.
• Process Lifecycle: Real-time tracking of processes through five fundamental states: New, Ready, Running, Waiting (Blocked), and Terminated.
2. Concurrency Management
Implementation of the Producer-Consumer model to synchronize traffic sensors and analysis modules.
• Semaphores (Mutex): Uses binary and counting semaphores to ensure mutual exclusion and prevent race conditions when accessing shared data buffers.
• Deadlock Prevention: Design strategies to ensure the system remains stable and robust, even under extreme processing demands.
Technical Foundation & Architecture
Hardware Modeling
The simulator's performance is cimented in an understanding of underlying hardware architectures:
• Von Neumann Bottleneck: Models the latency caused by a unified memory for instructions and data, where both compete for a shared bus—akin to a "single-lane highway".
• Harvard Architecture: Integrates principles of independent buses and memories for instructions and data, providing the predictability and concurrent access required for real-time signal processing.
Real Parallelism vs. Pseudoparallelism
While older systems were limited to pseudoparallelism (interleaving tasks on a single core), SIGET is designed for real parallelism through multithreading. By executing different threads of a process simultaneously on multi-core hardware, the system maximizes performance and availability.
Implementation Details
• Language: Python 3.x.
• Key Libraries:
    ◦ threading: To achieve concurrency and manage task sequences within a process.
    ◦ time: To simulate CPU bursts and represent the flow of data through system buses.
    ◦ random: Used to emulate unpredictable I/O blocking events (Waiting state).
How to Run
1. Clone the repository:
2. Run the scheduling simulator:
3. Run the concurrency module:
Conclusions
The SIGET project demonstrates that efficient process management transforms a developer from a "code writer" into a Software Solutions Architect. By applying robust scheduling and synchronization mechanisms, we ensure the stability and security of critical urban infrastructure.# concurrencia_siget