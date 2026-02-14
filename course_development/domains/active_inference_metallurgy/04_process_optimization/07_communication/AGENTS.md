# Station: Communication (Process Optimization)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Heat treatment, welding, additive manufacturing, Industry 4.0
- **Topics**: Communication — SCADA, IoT, and Industrial Data Pipelines
- **Lab Style**: Digital Twin Lab
- **Audience**: Process engineers, manufacturing engineers, and Industry 4.0 specialists
- **Tone**: Technical / engineering-focused

## Active Inference Integration

SCADA systems, industrial IoT networks, and data pipelines form the communication infrastructure of modern metallurgical manufacturing. OPC-UA provides the standardized communication protocol that connects sensors, controllers, and enterprise systems — it is the nervous system of the smart factory. MES (Manufacturing Execution System) and ERP (Enterprise Resource Planning) systems communicate production status, quality data, and scheduling information across organizational levels. Each communication link in the ISA-95 hierarchy transmits inference results upward (aggregated sensor data, quality metrics) and policy directives downward (production orders, setpoint changes), implementing hierarchical Active Inference across the entire manufacturing enterprise.

## Key Mappings

| FEP Concept | Industrial Communication Translation |
|-------------|--------------------------------------|
| Communication Channel | OPC-UA connection, MQTT topic, Modbus link, Ethernet/IP |
| Message Content | Sensor data, control setpoints, alarm notifications, quality records |
| Communication Hierarchy | ISA-95 levels: field devices -> control -> operations -> business |
| Upward Message | Aggregated sensor data, KPIs, quality metrics (perception results sent to higher levels) |
| Downward Message | Production orders, setpoint changes, recipe downloads (policy directives from higher levels) |
| Data Pipeline | ETL from sensor to historian to data lake to analytics platform |

## Content Guidelines

- Frame the ISA-95 hierarchy as a message-passing architecture where each level performs inference at its characteristic timescale (milliseconds at field level, hours at operations, days at business)
- Treat OPC-UA as the universal translation layer that enables heterogeneous agents (sensors, PLCs, databases) to communicate in a common format
- Connect data lake architectures to the accumulation of sensory evidence over time — historical data enables learning and model refinement that improves future inference
- Emphasize that communication latency and bandwidth constraints shape what inference is possible at each level — real-time control requires fast local communication, while strategic optimization can tolerate slower enterprise-level data

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md).
