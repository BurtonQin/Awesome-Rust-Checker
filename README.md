# Awesome Rust checkers

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

> Contributions welcomed!

## Table of contents

- [Awesome Rust checkers](#awesome-rust-checkers)
  - [Table of contents](#table-of-contents)
  - [Linters](#linters)
  - [Static Checkers](#static-checkers)
  - [Dynamic Checkers](#dynamic-checkers)
  - [Verifiers](#verifiers)

## Linters

| Name | Description | Working on | Bug types | Technology | Last Commit Time |
| -----| ----------- | ---------- | ----------| -----------| ----------- |
| [clippy](https://github.com/rust-lang/rust-clippy) | A bunch of lints to catch common mistakes and improve your Rust code. Paper: [ICSE-Companion'24](https://dl.acm.org/doi/abs/10.1145/3639478.3643096) | HIR | Versatile | Pattern matching | 2025-04-06 |
| [dylint](https://github.com/trailofbits/dylint) | Run Rust lints from dynamic libraries | HIR | Versatile | Pattern matching | 2025-04-07 |

## Static Checkers

| Name | Description | Working on | Bug Types | Technology | Maintenance |
| -----| ----------- | ---------- | ----------|-----------| ----------- |
| [MIRAI](https://github.com/endorlabs/MIRAI) | Rust mid-level IR Abstract Interpreter | MIR | Panic, Security bugs, Correctness | Abstract Interpretation | 2025-03-04 |
| [lockbud](https://github.com/BurtonQin/lockbud) | Statically detect common memory and concurrrency bugs in Rust. Paper: [Safety Issues in Rust, TSE'24](https://songlh.github.io/paper/rust-tse.pdf) | MIR | Double-Lock, Conflicting-Lock-Order, Atomicity-Violation, Use-After-Free, Invalid-Free, Panic Locations | Data-flow Analysis | 2025-04-04 |
|[RAP (formerly SafeDrop)](https://github.com/Artisan-Lab/RAP) | Rust Analysis Platform. Paper: [SafeDrop, TOSEM'22](https://dl.acm.org/doi/10.1145/3542948) | MIR | Use-After-Free, Double-Free | Data-flow Analysis | 2025-04-07 |
|[RCanary](https://github.com/Artisan-Lab/rCanary) | Detecting Memory Leaks Across Semi-automated Memory Management Boundary in Rust. [RCanary, TSE'24](https://arxiv.org/pdf/2308.04787) | HIR, MIR | Memory Leaks | Static Program Analysis, Model Checking | 2023-09-11 |
|[Rudra](https://github.com/sslab-gatech/Rudra)| Rust Memory Safety & Undefined Behavior Detection. Paper: [Rudra, SOSP'21](https://dl.acm.org/doi/abs/10.1145/3477132.3483570) | HIR, MIR | Memory safety when panicked, Higher Order Invariant, Send Sync Variance | Data-flow Analysis | 2024-02-12 |
|[Yuga](https://github.com/vnrst/Yuga) | Automatically Detecting Lifetime Annotation Bugs in the Rust Language. Paper: [Yuga, ICSE'24](https://arxiv.org/abs/2310.08507) | HIR, MIR |  Lifetime Annotation Bugs | Data-flow Analysis | 2024-04-01 |
|[MirChecker](https://github.com/lizhuohua/rust-mir-checker)| A Simple Static Analysis Tool for Rust. Paper: [MirChecker, CCS'21](https://dl.acm.org/doi/10.1145/3460120.3484541) | MIR | Panic (including numerical), Lifetime Corruption (memory issues) | Abstract Interpretation | 2024-05-24 |
|[FFIChecker](https://github.com/lizhuohua/rust-ffi-checker) | A Static Analysis Tool For Detecting Memory Management Bugs Between Rust and C/C++. Paper: [FFIChecker, ESORICS'22](https://dl.acm.org/doi/10.1007/978-3-031-17143-7_33) | LLVM IR | Memory issues across the Rust/C FFI | Abstract Interpretation | 2022-05-31 |
|[RUPTA](https://github.com/rustanlys/rupta) | Supports pointer/alias analysis for Rust, operating on Rust MIR. It currently offers callsite-based pointer analysis. Paper: [RUPTA, CC'24](https://dl.acm.org/doi/10.1145/3640537.3641574) | MIR | Not bugs, for callgraph construction| Callsite-based pointer analysis | 2025-02-01 |
|[Charon](https://github.com/AeneasVerif/charon) | Interface with the rustc compiler for the purpose of program verification. Paper: [Charon](https://arxiv.org/abs/2410.18042) | MIR, LLBC | An Analysis Framework for Rust | Convert MIR to LLBC for analysis | 2025-04-06 |
|[Cocoon](https://github.com/PLaSSticity/Cocoon-implementation) | Static Information Flow Control in Rust. Paper: [Cocoon, OOPSLA'24](https://dl.acm.org/doi/pdf/10.1145/3649817) | Rust Soure Code | Secrecy Leaks | Rust’s type system and procedural macros  | 2024-03-20 |
|[rustsp_analyzer](https://github.com/Artisan-Lab/rustsp_analyzer) | Fearless Unsafe. A More User-friendly Document for Unsafe Rust Programming Base on Refined Safety Properties. Paper: [Fearless Unsafe](https://arxiv.org/pdf/2412.06251) | HIR | Safety Properties | Summarization | 2025-01-01 |
|[AtomVChecker](https://github.com/AtomVChecker/rust-atomic-study/tree/main/section-5-detection/AtomVChecker) | Statically detect memory ordering misuses for Rust. Paper: [AtomVChecker, ISSRE'24](https://ieeexplore.ieee.org/document/10771495) | MIR | Atomic concurrency bugs and performance loss due to memory ordering misuse | Data-flow Analysis | 2024-09-12 |
|[rustowl](https://github.com/cordx56/rustowl)| Visualize ownership and lifetimes in Rust for debugging and optimization | MIR | Lifetime Errors | Rust’s borrow checker | 2025-04-07 |
|[pinchecker](https://github.com/yxdai-nju/pinchecker) | Contract Violation detection tool for Rust crates | MIR, [PLIR](https://github.com/yxdai-nju/mir2rpil) | unsafe code that fails to uphold its safety requirements | - | 2025-03-04 |
|[mirilli](https://github.com/icmccorm/mirilli)| A study of undefined behavior across foreign function boundaries in Rust libraries | MIR, LLVM IR | UB across FFI boundaries | - | 2025-02-13 |

Academic Papers (source code not found yet)

| Name | Description | Working on | Bug Types | Technology |
| -----| ----------- | ---------- | ----------|----------- |
| Rupair | Rupair: Towards Automatic Buffer Overflow Detection and Rectification for Rust. [Rupair, ACSAC'21](https://dl.acm.org/doi/abs/10.1145/3485832.3485841) | AST, MIR | Buffer Overflow | Data-flow Analysis |
| CRUST| CRUST: Towards a Unified Cross-Language Program Analysis Framework for Rust. [CRUST, QRS'22](https://ieeexplore.ieee.org/document/10062430) | CRustIR based on MIR | Security (CFI vilation, Meta Data Leaking, Format String Attack), Memory issues(Out-of-bounds, Use-after-Free, Double-Free, Stack-Overflow, Buffer-Overflow), Arithmetic (Divide-by-zero, Integer-Overflow) | Program Analysis Framework |
| ACORN | ACORN: Towards a Holistic Cross-Language Program Analysis for Rust. [ACORN](https://csslab-ustc.github.io/publications/2023/acorn.pdf) | Wasm | Security (Tainted Variable, Dangerous Function, Format String Attack), Memory issues (Out-of-bounds, Use-after-Free, Double-Free, Stack-Overflow, Buffer-Overflow), Arithmetic (Divide-by-zero, Integer-Overflow)  | Program Analysis Framework |
| Yu Zhang | Static Deadlock Detection for Rust Programs. [Yu Zhang](https://arxiv.org/abs/2401.01114) | MIR | Deadlock | Data-flow Analysis |
| Kaiwen Zhang | Automatically Transform Rust Source to Petri Nets for Checking Deadlocks. [Kaiwen Zhang](https://arxiv.org/abs/2212.02754) | MIR | Deadlock | Petri Nets |
| RustC4 | Leveraging Large Language Model to Assist Detecting Rust Code Comment Inconsistency. [ASE'24](https://dl.acm.org/doi/10.1145/3691620.3695010) | AST | Code Comment Inconsistency | LLM |
| craft | Automated Fault Tree Generation for Rust Programs. [EDCC'24](https://doi.ieeecomputersociety.org/10.1109/EDCC61798.2024.00022) | - | Fault Tree |  Static Program Analysis |
| PanicFI | An Infrastructure for Fixing Panic Bugs in Real-World Rust Programs. [PanicFI](https://www.arxiv.org/pdf/2408.03262) | HIR, AST | Fixing Panic Bugs |  Pattern Matching |

## Dynamic Checkers

| Name | Description | Working on | Bug Types | Technology | Last Commit Time |
| -----| ----------- | ---------- | ----------| -----------| ----------- |
| [miri](https://github.com/rust-lang/miri) | An interpreter for Rust's mid-level intermediate representation | MIR | Undefined Behavior | Abstract Interpretation | 2025-04-07 |
| [cargo-careful](https://github.com/RalfJung/cargo-careful) | Execute Rust code carefully, with extra checking along the way | - | Undefined Behavior | Enable Debug Assertion in std | 2024-08-10 |
| [cargo-fuzz](https://github.com/rust-fuzz/cargo-fuzz) | Command line helpers for fuzzing | - | - | Fuzzing | 2025-03-11 |
| [Loom](https://github.com/tokio-rs/loom)| Concurrency permutation testing tool for Rust. | Source Code | Concurrency Bugs | Permutation testing | 2025-02-11 |
| [Shuttle](https://github.com/awslabs/shuttle) | A library for testing concurrent Rust code. Paper [A Randomized Scheduler with Probabilistic Guarantees of Finding Bugs](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/asplos277-pct.pdf) | Source Code | Concurrency Bugs | Randomized testing | 2025-03-31 |
| [ERASAN](https://github.com/S2-Lab/ERASan) | Efficient Rust Address Sanitizer. Paper: [IEEES&P'24](https://www.computer.org/csdl/proceedings-article/sp/2024/313000a239/1WPcYZde4BW) | - | Memory Access Bugs | Fuzzing | 2024-07-10 |
| [Automated-Fuzzer](https://github.com/qarmin/Automated-Fuzzer) | Simple tool to create broken files and checking them with special apps | - | Panic | Fuzzing | 2025-02-24 |
| [RULF](https://github.com/Artisan-Lab/RULF)| Fuzz Target Generator for Rust libraries. Paper: [RULF, ASE'21](https://dl.acm.org/doi/abs/10.1109/ASE51524.2021.9678813) | - | Out-of-bound, Panic (including arithmetic) | Fuzzing | 2023-11-09 |
| [RPG](https://github.com/wcventure/PERIOD)<sup>1</sup>| RPG: Rust Library Fuzzing with Pool-based Fuzz Target. Paper: [RPG, ICSE'24](https://dl.acm.org/doi/10.1145/3597503.3639102) | - | Out-of-bound, Panic (including arithmetic) | Fuzzing | 2022-10-09 |
| [SyRust](https://kilthub.cmu.edu/articles/code/SyRust_Artifact_PLDI2021_Artifact/14356976) | Automatic Testing of Rust Libraries with Semantic-Aware Program Synthesis. Paper: [SyRust, PLDI'21](https://dl.acm.org/doi/pdf/10.1145/3453483.3454084)| - | - | Program Synthesis | 2021-04-14 |
| [NADER](https://zenodo.org/records/5484436)| Automatic Context-Aware Safety Enhancement for Rust. Paper: [OOPSLA'21](https://dl.acm.org/doi/pdf/10.1145/3485480) | MIR, Source Code | Unchecked Indexing | API Replacing | 2021-07-13 |
| [casr](https://github.com/ispras/casr)<sup>2</sup> | collect crash (or UndefinedBehaviorSanitizer error) reports, triage, and estimate severity. Paper: [Casr-Cluster, ISPRAS'21](https://www.doi.org/10.1109/ISPRAS53967.2021.00012), [Ivannikov Memorial Workshop'24](https://arxiv.org/abs/2405.18174)| Crash Reports from ASan, UBSan, GDB | - | Analyze crashes| 2025-04-07 |
| [FRIES](https://github.com/SSCT-Lab/FRIES) | Fuzzing Rust Library Interactions via Efficient Ecosystem-Guided Target Generation. Paper: [FRIES, ISSTA'24](https://dl.acm.org/doi/pdf/10.1145/3650212.3680348) | MIR | Rust API interactions | Fuzzing | 2023-08-02 |
|[rustsmith](https://github.com/rustsmith/rustsmith) | A randomized program fuzzer for the Rust programming language. Paper: [rustsmith, ISSTA'23](https://rustsmith.github.io/docs/rustsmith-paper.pdf) [rustsmith, thesis](https://rustsmith.github.io/docs/rustsmith-thesis.pdf) | AST | Rust compiler bugs | Differential testing | 2023-07-21 |
|[rustlantis](https://github.com/cbeuw/rustlantis) | UB-free and deterministic rustc fuzzer. Paper: [rustlantis, OOPSLA'24](https://dl.acm.org/doi/pdf/10.1145/3689780)| MIR | Rust compiler bugs | Differential testing | 2025-01-17 |
|[RuMono](https://github.com/Artisan-Lab/RULF/tree/RuMono) | A fully automated Rust fuzz driver generator. Paper: [RuMono, TOSEM'24](https://dl.acm.org/doi/abs/10.1145/3709359) | - | Generic APIs | Fuzzing | 2023-11-09 |
| [rtsan-standalone-rs](https://github.com/realtime-sanitizer/rtsan-standalone-rs) | Standalone RealtimeSanitizer for Rust. [Blogpost](https://steck.tech/posts/rtsan-in-rust/) | Soure Code | Real-time Violations | LLVM  | 2025-03-10 |

Academic Papers (source code not found yet)

| Name | Description | Working on | Bug Types | Technology |
| -----| ----------- | ---------- | ----------|----------- |
| CrabSandwich | CrabSandwich: Fuzzing Rust with Rust. [CrabSandwich, Fuzzing'23](https://dl.acm.org/doi/abs/10.1145/3605157.3605176)| LLVM IR | Out-of-bounds, Panic | Fuzzing |
| Zhiyong Ren | Detect Stack Overflow Bugs in Rust via Improved Fuzzing Technique. [Zhiyong Ren, SEKE'21](https://dl.acm.org/doi/abs/10.1145/3485832.3485841) | AST, HIR, MIR, LLVM IR | Stack Overflow | Fuzzing |
| Rustcheck | Safety Enhancement of Unsafe Rust via Dynamic Program Analysis. [Rustcheck, QRS-C'23](https://ieeexplore.ieee.org/document/10429951) | MIR | Memory vulnerabilities | Static Program Analysis, Instrumentation |
| RUSTY | A Fuzzing Tool for Rust. [Poster@ACSAC'20](https://www.acsac.org/2020/program/poster-wips/2020-3-RUSTY%20%20A%20Fuzzing%20Tool%20for%20Rust.pdf) | - | Vulnerabilities | Fuzzing, Concolic Testing, Property-based Testing |
| Rust-twins | Automatic Rust Compiler Testing through Program Mutation and Dual Macros Generation. [ASE'24](https://wzyang.cn/files/Rust_twins.pdf) | AST, HIR | Rust compiler crashes and differences  | Differential testing, mutation, macroize components, LLM |
| SafeFFI | Poster: Ensuring Memory Safety for the Transition from C/C++ to Rust. [NDSS'24](https://www.ndss-symposium.org/wp-content/uploads/ndss24-posters-37.pdf)| LLVM IR | Memory safety in C/C++ and Rust Mixed Code | Existing sanitiers: HWASAN, SoftBound/CETS |


1. The link may be incorrect. See [here](https://wcventure.github.io/EnPage/opensource/2023-12-05-RPG).
2. casr analyze the results of dynamic checkers instead of performing dynamic analysis itself. Thanks [zjp-CN](https://github.com/zjp-CN) for recommending casr.

## Verifiers

| Name | Description | Working on | Bug Types | Technology | Last Commit Time |
| -----| ----------- | ---------- | ----------| -----------| ----------- |
| [kani](https://github.com/model-checking/kani/) | The Kani Rust Verifier is a bit-precise model checker for Rust. Paper: [kani, ICSE-SEIP'22](https://dl.acm.org/doi/abs/10.1145/3510457.3513031)| MIR | Memory safety, User-specified assertions, Panics, Unexpected behavior (e.g., arithmetic overflows)  | Model Checking | 2025-04-04 |
| [prusti](https://github.com/viperproject/prusti-dev) | A static verifier for Rust, based on the Viper verification infrastructure. Paper: [prusti, NFM'22 ](https://link.springer.com/chapter/10.1007/978-3-031-06773-0_5) | Viper | Panic (inluding arithmetic), User-specified assertions | Symbolic Execution  | 2024-03-26 |
| [crux-mir](https://github.com/GaloisInc/crucible/tree/master/crux-mir) | A static simulator for Rust programs. Paper: [crux](https://arxiv.org/abs/2410.18280) | - | - | Symbolic Testing | 2025-04-04 |
| [verus](https://github.com/verus-lang/verus) | Verified Rust for low-level systems code. Paper: [verus, OOPSLA'23](https://dl.acm.org/doi/pdf/10.1145/3586037), [SOSP'24](https://www.microsoft.com/en-us/research/publication/verus-a-practical-foundation-for-systems-verification/) | - | - | SMT-based Verification<sup>5</sup> | 2025-04-07 |
| [flux](https://github.com/flux-rs/flux) | flux is a refinement type checker for Rust. Paper: [flux, PLDI'23](https://dl.acm.org/doi/10.1145/3591283)| - | - | - | 2025-04-07 |
| [Aeneas](https://github.com/AeneasVerif/aeneas) | A verification toolchain for Rust programs. Paper: [Aeneas, ICFP'22](https://dl.acm.org/doi/abs/10.1145/3547647), [ICFP'24](https://dl.acm.org/doi/abs/10.1145/3674640) | LLBC (for safe Rust only) | - | - | 2025-04-05 |
| [hax](https://github.com/cryspen/hax) | A Rust verification tool. [Publications](https://hax.cryspen.com/publications.html) | - | Panic, Properties, Data Invariants | Translationn to F* or Rocq | 2025-04-03 |
| [RustBelt](https://gitlab.mpi-sws.org/iris/lambda-rust/) | Formal (and machine-checked) safety proof for a language representing a realistic subset of Rust. Paper: [RustBelt, POPL'18](https://dl.acm.org/doi/10.1145/3158154) | 𝜆Rust| - | - | 2024-12-13 |
| [RustHorn](https://github.com/hopv/rust-horn) | A CHC-based automated verifier for Rust [RustHorn, TOPLAS'21](https://dl.acm.org/doi/full/10.1145/3462205) | MIR | - | - | 2024-08-27 |
| [Creusot](https://github.com/creusot-rs/creusot) | A deductive verifier for Rust code. [Creusot, ICFEM'22](https://inria.hal.science/hal-03737878/file/main.pdf) | WhyML | Panics, overflows, Assertion failures | Deductive Verification | 2025-04-03 |
| [RustHornBelt](https://gitlab.mpi-sws.org/iris/lambda-rust/-/tree/masters/rusthornbelt) | A Semantic Foundation for Functional Verification of Rust Programs with Unsafe Code. Paper: [RustHornBelt, PLDI'22](https://dl.acm.org/doi/10.1145/3519939.3523704)| 𝜆Rust | - | - | 2023-02-14 |
| [RefinedRust<sup>1</sup>](https://gitlab.mpi-sws.org/lgaeher/refinedrust-dev) | A Type System for High-Assurance Verification of Rust Programs. Paper: [RefinedRust, PLDI'24](https://dl.acm.org/doi/10.1145/3656422)| Radium | - | - | 2025-01-03 |
| [VeriFast<sup>2</sup>](https://github.com/verifast/verifast) | Research prototype tool for modular formal verification of C and Java programs. Paper: [VeriFast, NFM'11](https://doi.org/10.1007/978-3-642-20398-5_4)| - | - | Symbolic Execution | 2025-04-07 |
| [mendel-verifier](https://github.com/viperproject/mendel-verifier) | Capability-based verifier for safe Rust clients of interior mutability. Paper: [Poli](https://arxiv.org/abs/2405.08372), [Thesis](https://www.research-collection.ethz.ch/bitstream/handle/20.500.11850/703796/Poli2024.pdf?sequence=3&isAllowed=y)| Viper | Interior Mutability | Symbolic Execution | 2024-07-16 |
| [silver-sif-extension](https://github.com/viperproject/silver-sif-extension) | Extension of the Viper language with modular product programs and information flow specifications. Paper: [Thesis](https://ethz.ch/content/dam/ethz/special-interest/infk/chair-program-method/pm/documents/Education/Theses/Till_Arnold_MA_Report.pdf)| Viper | Differential Privacy | Symbolic Execution | 2025-04-04 |

Academic Papers (source code not found yet)

| Name | Description | Working on | Bug Types | Technology |
| -----| ----------- | ---------- | ----------|----------- |
| GillianRust | A hybrid approach to semi-automated Rust verification. [GillianRust](https://arxiv.org/abs/2403.15122)| Unsafe Code Supported | - | Separation Logic based Hybrid Verification<sup>5</sup> |
| UnsafeCop | Towards Memory Safety for Real-World Unsafe Rust Code with Practical Bounded Model checking. [UnsafeCop, FM'24](https://link.springer.com/chapter/10.1007/978-3-031-71177-0_19)| - | Memory safety issues | Bounded Model Checking |
| SAFE | Automated Proof Generation for Rust Code via Self-Evolution. [SAFE](https://arxiv.org/abs/2410.15756) | Rust Code With Docstring, Verus | - | Verus Verifier, LLM |
| PanicCheck | Broadly Enabling KLEE to Effortlessly Find Unrecoverable Errors. [PanicCheck, ICSE-SEIP'24](https://doi.org/10.1145/3639477.3639714) | LLVM IR | Panic | KLEE |

1. Thanks to [jedbrown](https://users.rust-lang.org/u/jedbrown) for recommending RefinedRust and other Rust-related verification tools.
2. Rust support is WIP in VeriFast. Thanks [zjp-CN](https://github.com/zjp-CN) for recommending VeriFast.

Thanks to the following awesome works:

1. https://github.com/analysis-tools-dev/static-analysis?tab=readme-ov-file#rust
2.  https://github.com/analysis-tools-dev/dynamic-analysis?tab=readme-ov-file#rust
3. [A Survey of Rust Language Security Research](https://link.oversea.cnki.net/doi/10.19363/J.cnki.cn10-1380/tn.2023.11.06)
4. [RefinedRust: A Type System for High-Assurance Verification of Rust Programs](https://dl.acm.org/doi/10.1145/3656422)
5. [Verifying the Rust Standard Library](https://www.soundandcomplete.org/vstte2024/vstte2024-invited.pdf)
